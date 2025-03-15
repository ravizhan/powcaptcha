import random


class PrimeGenerator:
    def __init__(self, bits):
        self.bits = bits

    def generate(self):
        p = self.generate_prime()
        q = self.generate_prime()
        return p * q, p, q

    def generate_prime(self):
        while True:
            num = random.getrandbits(self.bits)
            if self.is_prime(num):
                return num

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            if n % p == 0:
                return n == p
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            if a >= n:
                continue
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
