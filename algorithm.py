from representations import IntegerRepresentation

def extendedEuclidAlgorithm(a, b):
    """ 
    Takes two objects of the same type that inherits from the class DivisibleObject,
    and applies the extended euclidean algorithm.
    
    Returns a tupple (gcd, s, t) where gcd is the gcd(a,b), and s, t satisfy the
    equation s*a + t*b = gcd(a,b)
    """
    s1, s2 = a.get_multiplicative_identity(), a.get_zero_element()
    t1, t2 = a.get_zero_element() , a.get_multiplicative_identity()
    while not b.is_zero():
        quotient, remainder = divmod(a, b)
        a = b
        b = remainder
        s1, s2 = s2, s1 - quotient*s2
        t1, t2 = t2, t1 - quotient*t2
    return a, s1, t1
