import unittest
from powcaptcha import PowCaptcha

class MyTestCase(unittest.TestCase):
    def test_solve(self):
        captcha = PowCaptcha("http://localhost:8000")
        result = captcha.solve()
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
