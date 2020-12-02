import unittest
from math import gcd
from algorithm import *
from representations import *

import random
random.seed(1)

class TestIntegers(unittest.TestCase):
    def test_under_hundreds(self):
        """ Compares math.gcd with my gcd function for every pair of integers i,j | i,j < 100
        are less than 100 """
        for i in range(1, 100):
            for j in range(1, 100):
                with self.subTest(i=i, j=j):
                    my_gcd, t, s = extendedEuclidAlgorithm(IntegerRepresentation(i), IntegerRepresentation(j))
                    msg1 = f"math.gcd({i}, {j}) didn't match our gcd of {my_gcd}."
                    msg2 = f"math.gcd({i}, {j}) didn't equal {t}*{i} + {s}*{j}"
                    self.assertEqual(gcd(i,j), my_gcd, msg=msg1)
                    self.assertEqual(gcd(i,j), t*i + s*j, msg=msg2)

    def test_largecase_1(self):
        """ a = 978, b = 89798763754892653453379597352537489494736 """
        i = 978
        j = 89798763754892653453379597352537489494736

        my_gcd, t, s = extendedEuclidAlgorithm(IntegerRepresentation(i), IntegerRepresentation(j))
        msg1 = f"math.gcd({i}, {j}) didn't match our gcd of {my_gcd}."
        msg2 = f"math.gcd({i}, {j}) didn't equal {t}*{i} + {s}*{j}"
        self.assertEqual(gcd(i,j), my_gcd, msg=msg1)
        self.assertEqual(gcd(i,j), t*i + s*j, msg=msg2)

    def test_largecase_2(self):
        """ a = 1221, b = 1234567891011121314151617181920212223242526272829 """
        i = 1221
        j = 1234567891011121314151617181920212223242526272829

        my_gcd, t, s = extendedEuclidAlgorithm(IntegerRepresentation(i), IntegerRepresentation(j))
        msg1 = f"math.gcd({i}, {j}) didn't match our gcd of {my_gcd}."
        msg2 = f"math.gcd({i}, {j}) didn't equal {t}*{i} + {s}*{j}"
        self.assertEqual(gcd(i,j), my_gcd, msg=msg1)
        self.assertEqual(gcd(i,j), t*i + s*j, msg=msg2)

class TestGaussianIntegers(unittest.TestCase):
    def test_case1(self):
        """ a = 16+7i and b = 10-5i """
        a = GaussianIntegerRepresentation(16, 7)
        b = GaussianIntegerRepresentation(10, -5)
        correct_gcd = GaussianIntegerRepresentation(1, 2)
        my_gcd, t, s = extendedEuclidAlgorithm(a, b)
        msg = f"Computed gcd({a}, {b}) = {my_gcd} was incorrect. Answer: {correct_gcd}"
        msg2 = f"{t}*{a} + {s}*{a} didn't equal computed gcd {my_gcd}"
        self.assertEqual(my_gcd, correct_gcd, msg)

class TestEisensteinIntegers(unittest.TestCase):
    def test_bezouts_coefficients(self):
        for a, b in self.generate_eisenstein_pairs(100):
            my_gcd, t, s = extendedEuclidAlgorithm(a, b)
            msg1 = f"{t}*{a} + {s}*{a} didn't equal computed gcd {my_gcd}"
            self.assertEqual(type(my_gcd), EisensteinIntegerRepresentation, msg="Something aint right")
            self.assertEqual(my_gcd, t*a + s*b, msg=msg1)
    
    def generate_eisenstein_pairs(self, n):
        """ Generator that yields n pairs of eisenstein numbers """
        for i in range(n):
            a = random.randrange(-10000,10000)
            b = random.randrange(-10000,10000)
            c = random.randrange(-10000,10000)
            d = random.randrange(-10000,10000)
            first = EisensteinIntegerRepresentation(a, b)
            second = EisensteinIntegerRepresentation(c, d)
            yield (first, second)

if __name__ == '__main__':
    unittest.main()