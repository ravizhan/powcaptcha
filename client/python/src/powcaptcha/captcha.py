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
            self.challenge = req.json()["challenge"]
            return self.challenge
        else:
            return None

    def solve_challenge(self) -> None|list:
        n = self.challenge["question"]
        factors = self.prime_challenge.calc(n)
        if len(factors) == 2 and factors[0] * factors[1] == n:
            return sorted(factors)
        else:
            return None

    def submit_answer(self, answer: list):
        data = {
            "challenge": {
                "id": self.challenge["id"],
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
            answer = self.solve_challenge()
        result = self.submit_answer(answer)
        return result
