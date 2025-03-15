import json
from typing import Annotated

import redis
from fastapi import FastAPI, Header, Request
from fastapi.responses import Response,JSONResponse
import jwt,uuid
from models import *
from utils import PrimeGenerator

app = FastAPI()
with open("config.json") as f:
        config = json.load(f)
r = redis.Redis(
    connection_pool=redis.ConnectionPool(
        host=config["redis"]["host"],
        port=config["redis"]["port"],
        db=config["redis"]["db"],
        password=config["redis"]["password"]
    )
)
prime_generator = PrimeGenerator(config["difficulty"])
secret_key = config["secret"]

@app.get("/request_challenge", response_model=RequestChallenge)
def request_challenge(request: Request, user_agent: Annotated[str, Header()]):
    if user_agent == "":
        return Response(status_code=403)
    challenge,a1,a2 = prime_generator.generate()
    challenge_id = str(uuid.uuid4())
    data = {
        "challenge": {
            "id": challenge_id,
            "answer": sorted([a1,a2])
        },
        "ip": request.client.host,
        "ua": user_agent
    }
    r.set(challenge_id, json.dumps(data), ex=60)
    resp = {
        "challenge": {
            "id": challenge_id,
            "question": challenge
        }
    }
    return resp

@app.post("/submit_answer")
def submit_answer(data: SubmitChallenge):
    answer = data.challenge.answer
    try:
        redis_data = json.loads(r.get(data.challenge.id))
    except:
        return {"message": "Invalid challenge id"}
    r.expire(data.challenge.id, 60)
    for i in range(len(answer)):
        if answer[i] != redis_data["challenge"]["answer"][i]:
            return {"message": "Incorrect answer"}
    jwt_token = jwt.encode({"challenge_id": data.challenge.id, "ip": redis_data["ip"], "ua": redis_data["ua"]},secret_key)
    return {"message": "Correct answer", "token": jwt_token}

@app.post("/verify_token")
def verify_token(data: VerifyToken):
    jwt_data = jwt.decode(data.token, secret_key, algorithms=["HS256"])
    if r.get(jwt_data["challenge_id"]) is not None:
        return {"message": "Token is valid"}
    else:
        return JSONResponse({"message": "Token is invalid"}, status_code=403)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)