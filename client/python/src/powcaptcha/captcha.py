import httpx
from .utils import *

class PowCaptcha:
    def __init__(self, base_url):
        self.challenge = None
        self.base_url = base_url
        self.session = httpx.Client(base_url=base_url)
        self.prime_challenge = PrimeChallenge()

    def request(self):
        self.challenge = None
        req = self.session.get("/request_challenge")
        if req.status_code == 200:
            return req.json()["challenge"]
        else:
            return None

    def solve_challenge(self, challenge) -> None|list:
        n = int(challenge["question"])
        factors = self.prime_challenge.calc(int(n))
        if len(factors) == 2 and factors[0] * factors[1] == n:
            return [str(i) for i in sorted(factors)]
        else:
            return None

    def submit_answer(self, challenge_id, answer: list):
        data = {
            "challenge": {
                "id": challenge_id,
                "answer": answer
            },
        }
        req = self.session.post("/submit_answer", json=data)
        if req.status_code == 200:
            return req.json()["token"]
        else:
            return None

    def solve(self) -> str|None:
        challenge = self.request()
        if challenge is None:
            return None
        else:
            answer = self.solve_challenge(challenge)
        result = self.submit_answer(challenge["id"], answer)
        return result
