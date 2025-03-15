import random


class PrimeChallenge:
    def __init__(self):
        pass

    def calc(self, num):
        return self.factorize(num)

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

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

    def brent_rho(self, n):
        if n % 2 == 0:
            return 2
        if n % 3 == 0:
            return 3
        if n % 5 == 0:
            return 5
        y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
        r, q, g = 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (pow(y, 2, n) + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (pow(y, 2, n) + c) % n
                    q = q * abs(x - y) % n
                g = self.gcd(q, n)
                k += m
            r *= 2
        if g == n:
            while True:
                ys = (pow(ys, 2, n) + c) % n
                g = self.gcd(abs(x - ys), n)
                if g > 1:
                    break
        return g

    def factorize(self,n) -> list:
        factors = []
        def _factorize(n):
            if n == 1:
                return
            if self.is_prime(n):
                factors.append(n)
                return
            d = self.brent_rho(n)
            _factorize(d)
            _factorize(n // d)
        _factorize(n)
        return factors
