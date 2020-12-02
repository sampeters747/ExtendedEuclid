""" Classes that represent Z, Z[i], Z[omega]. Includes base parent class DivisibleObject that requires
div and mod methods be implemented. """

from math import ceil, floor, sqrt

# Base object
class DivisibleObject:
    # Requires that divmod method be defined in any class that inherits from this class
    def __divmod__(self, other):
        raise NotImplementedError()

    # Requires that multiplication method be defined in any class that inherits from this class
    def __mul__(self, other):
        raise NotImplementedError()

    # Requires that the subtract method be defined in any class that inherits from this class
    def __sub__(self, other):
        raise NotImplementedError()

    # Requires that the add method be defined in any class that inherits from this class
    def __add__(self, other):
        raise NotImplementedError()  

    # Requires that any subclass implements an is_zero() method to check if the object is the zero element
    def is_zero(self) -> bool:
        raise NotImplementedError()

    # Helpful methods that aren't strictly necessary, but make the program nicer
    def __str__(self):
        raise NotImplementedError()
    
    def __repr__(self):
        raise NotImplementedError()

    def __eq__(self):
        raise NotImplementedError()

    def get_zero_element(self):
        """ Returns a zero element of the same type """
        raise NotImplementedError()

    def get_multiplicative_identity(self):
        """ Returns a multiplicative identity of the same type """
        raise NotImplementedError()


class IntegerRepresentation(DivisibleObject):
    def __init__(self, a: int):
        # Holds value of integer
        self.a = a

    def __divmod__(self, other):
        quotient = IntegerRepresentation(self.a // other.a)
        remainder = IntegerRepresentation(self.a% other.a)
        return quotient, remainder

    def __mul__(self, other):
        if type(self) is type(other):
            new_value = self.a * other.a
            return IntegerRepresentation(new_value)
        elif type(other) is int:
            return self.a * other

    def __sub__(self, other):
        new_value = self.a-other.a
        return IntegerRepresentation(new_value)
    
    def __add__(self, other):
        new_value = self.a+other.a
        return IntegerRepresentation(new_value)

    def is_zero(self) -> bool:
        if self.a == 0:
            return True

    # Helper methods
    def __str__(self):
        return f"{self.a}"

    def __repr__(self):
        return f"{self.a}"

    def __eq__(self, other):
        if type(self) is type(other):
            return self.a == other.a
        else:
            return self.a == other

    def __gt__(self, other):
        return self.a > other.a

    def get_zero_element(self):
        """ Returns a zero element of the same type """
        return IntegerRepresentation(0)

    def get_multiplicative_identity(self):
        """ Returns a multiplicative identity of the same type """
        return IntegerRepresentation(1)


class GaussianIntegerRepresentation(DivisibleObject):
    """ Represents an imaginary number a + bi """
    def __init__(self, a: int, b: int):
        # Represents the real part of the number
        self.a = a
        # Represents the imaginary part of the number
        self.b = b

    def __divmod__(self, other):
        """ 
        Performs the division algorithm on self and other, returning a tupple
        (quotient, remainder)

        Based on: https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:complex/x9e81a4f98389efdf:complex-div/a/dividing-complex-numbers-review
        And https://fermatslasttheorem.blogspot.com/2005/06/division-algorithm-for-gaussian.html
        """
        # We're representing division as a fraction with two variables
        numerator = self
        denominator = other
        # Getting the conjugate of the denominator
        denom_conjugate = denominator.conjugate()
        # Multiplying both sides of the fraction by the conjugate of the numerator
        # This gets us a real number in the denominator
        numerator = numerator * denominator.conjugate()
        denominator = denominator * denominator.conjugate()
        # Dividing the numerator and denominator by the denominator
        numerator.a = numerator.a / denominator.a
        numerator.b = numerator.b / denominator.a
        denominator.a = denominator.a / denominator.a 
        # Rounding a to the nearest int
        if numerator.a % 1 > 0.5:
            qa = ceil(numerator.a)
        else:
            qa = floor(numerator.a)
        # Rounding b to the nearest int 
        if numerator.b % 1 > 0.5:
            qb = ceil(numerator.b)
        else:
            qb = floor(numerator.b)
        
        # Creating the quotient and remainder objects
        quotient = GaussianIntegerRepresentation(qa, qb)
        remainder = self-quotient*other
        return (quotient, remainder)


    def __mul__(self, other):
        """ Defines multiplication operation between two 
        complex numbers (a + bi)(c + di) = 
        ac + cbi + adi + bdi^2 = 
        (ac - bd) + (cb + ad)i
        
        Returns new guassian integer object
        """
        real = self.a * other.a - self.b * other.b
        imaginary = self.a * other.b + self.b * other.a
        return GaussianIntegerRepresentation(real, imaginary)

    def __sub__(self, other):
        """
        Defines subtraction operation between gaussian integers
        """
        real = self.a - other.a
        imaginary = self.b - other.b
        return GaussianIntegerRepresentation(real, imaginary)
    
    def __add__(self, other):
        """ Defines addition operation between gaussian integers """
        real = self.a + other.a
        imaginary = self.b + other.b
        return GaussianIntegerRepresentation(real, imaginary)

    def is_zero(self) -> bool:
        """ Checks if this is the zero element """
        return self.a == 0 and self.b == 0

    def get_zero_element(self):
        return GaussianIntegerRepresentation(0, 0)

    def get_multiplicative_identity(self):
        return GaussianIntegerRepresentation(1, 0)

    # Helper methods
    def __str__(self):
        return f"{self.a} + {self.b}i"

    def __repr__(self):
        return f"{self.a} + {self.b}i"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        return self.norm() > other.norm()

    def conjugate(self):
        return GaussianIntegerRepresentation(self.a, -self.b)

    def norm(self):
        conjugate = self.conjugate()
        return (self*conjugate).a

class EisensteinIntegerRepresentation(DivisibleObject):
    """ Represents a complex number a + bw where w = 
    (-1 + sqrt(3)i)/2
    """
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    # Requires that divmod method be defined in any class that inherits from this class
    def __divmod__(self, other):
        numerator = self
        denominator = other
        numerator = numerator * denominator.conjugate()
        denominator = denominator * denominator.conjugate()
        
        numerator.a = numerator.a / denominator.a
        numerator.b = numerator.b / denominator.a
        denominator.a = denominator.a / denominator.a 
        # Rounding a to the nearest int
        if numerator.a % 1 > 0.5:
            qa = ceil(numerator.a)
        else:
            qa = floor(numerator.a)
        # Rounding b to the nearest int 
        if numerator.b % 1 > 0.5:
            qb = ceil(numerator.b)
        else:
            qb = floor(numerator.b)
        
        # Creating the quotient and remainder objects
        quotient = EisensteinIntegerRepresentation(qa, qb)
        remainder = self-quotient*other
        return (quotient, remainder)

    def __mul__(self, other):
        a = self.a*other.a - self.b*other.b
        b = self.b*other.a + self.a*other.b - self.b*other.b
        return EisensteinIntegerRepresentation(a, b)

    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        return EisensteinIntegerRepresentation(a, b)

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return EisensteinIntegerRepresentation(a, b)

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def norm(self) -> int:
        """
        Returns the norm of the eisenstein integer.
        Based on https://proofwiki.org/wiki/Norm_of_Eisenstein_Integer
        """
        return self.a**2 - self.a*self.b + self.b**2

    def conjugate(self):
        return EisensteinIntegerRepresentation(self.a-self.b, -self.b)

    # Helpful methods that aren't strictly necessary, but make the program nicer
    def __str__(self):
        return f"{self.a} + {self.b}w"

    def __repr__(self):
        return f"{self.a} + {self.b}w"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def get_zero_element(self):
        """ Returns a zero element of the same type """
        return EisensteinIntegerRepresentation(0, 0)

    def get_multiplicative_identity(self):
        """ Returns a multiplicative identity of the same type """
        return EisensteinIntegerRepresentation(1, 0)
