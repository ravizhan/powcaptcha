from pydantic import BaseModel


class ChallengeBase(BaseModel):
    id: str

class RequestChallengeResponse(ChallengeBase):
    question: int

class SubmitChallengeRequest(ChallengeBase):
    answer: list[int]

class SubmitChallenge(BaseModel):
    challenge: SubmitChallengeRequest

class RequestChallenge(BaseModel):
    challenge: RequestChallengeResponse

class VerifyToken(BaseModel):
    token: str