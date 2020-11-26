def extendedEuclidAlgorithm(a, b):
    """ 
    Takes two objects of the same type that inherits from the class DivisibleObject,
    and applies the extended euclidean algorithm
    
    Returns a tupple (gcd, s, t) where gcd is the gcd(a,b), and s, t satisfy the
    equation s*a + t*b = gcd(a,b)
    """
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while b != 0:
        quotient = a // b
        remainder = a % b
        a = b
        b = remainder
        s1, s2 = s2, s1 - quotient*s2
        t1, t2 = t2, t1 - quotient*t2
    return a, s1, t1

a = 102
b = 38
answer, s, t = gcd(a,b)
print(answer, s*a+t*b)
assert s*a+t*b == answer