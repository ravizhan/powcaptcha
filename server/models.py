from pydantic import BaseModel


class ChallengeBase(BaseModel):
    id: str

class RequestChallengeResponse(ChallengeBase):
    question: str

class SubmitChallengeRequest(ChallengeBase):
    answer: list[str]

class SubmitChallenge(BaseModel):
    challenge: SubmitChallengeRequest

class RequestChallenge(BaseModel):
    challenge: RequestChallengeResponse

class VerifyToken(BaseModel):
    token: str