""" Classes that represent Z, Z[i], Z[omega]. Includes base parent class DivisibleObject that requires
div and mod methods be implemented. """

from math import ceil, sqrt

# Base object
class DivisibleObject:
    # Requires that divmod method be defined in any class that inherits from this class
    def __divmod__(self, other):
        raise NotImplementedError()
    # Requires that div method be defined in any class that inherits from this class
    def __truediv__(self, other):
        raise NotImplementedError()

    # Requires that multiplication method be defined in any class that inherits from this class
    def __mul__(self, other):
        raise NotImplementedError()

    # Requires that mod method be defined in any class that inherits from this class
    def __mod__(self, other):
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

    def get_zero_element(self):
        """ Returns a zero element of the same type """
        raise NotImplementedError()

    def get_multiplicative_identity(self):
        raise NotImplementedError()

    # Helpful methods that aren't strictly necessary, but make the program nicer
    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

    def __eq__(self):
        raise NotImplementedError()


class IntegerRepresentation(DivisibleObject):
    def __init__(self, a: int):
        # Holds value of integer
        self.a = a

    def __divmod__(self, other):
        quotient = IntegerRepresentation(self.a // other.a)
        remainder = IntegerRepresentation(self.a% other.a)
        return quotient, remainder

    def __truediv__(self, other):
        new_value = self.a // other.a
        return IntegerRepresentation(new_value)

    def __mul__(self, other):
        new_value = self.a * other.a
        return IntegerRepresentation(new_value)

    def __mod__(self, other):
        new_value = self.a%other.a
        return IntegerRepresentation(new_value)

    def __sub__(self, other):
        new_value = self.a-other.a
        return IntegerRepresentation(new_value)
    
    def __add__(self, other):
        new_value = self.a+other.a
        return IntegerRepresentation(new_value)

    def is_zero(self) -> bool:
        if self.a == 0:
            return True

    def get_zero_element(self):
        return IntegerRepresentation(0)

    def get_multiplicative_identity(self):
        return IntegerRepresentation(1)

    # Helper methods
    def __str__(self):
        return f"{self.a}"

    def __repr__(self):
        return f"{self.a}"

    def __eq__(self, other):
        return self.a == other.a

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
        """
        # We're representing division as a fraction with two variables
        numerator = self
        denominator = other
        # Getting the conjugate of the denominator
        denom_conjugate = denominator.conjugate()
        # Multiplying both sides of the fraction by the conjugate of the numerator
        # This gets us a real number in the denominator
        numerator = numerator * denom_conjugate
        denominator = denominator * denom_conjugate
        






    def __truediv__(self, other):
        """ Performs division between two gausian integers.
        Based on: https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:complex/x9e81a4f98389efdf:complex-div/a/dividing-complex-numbers-review
        And https://fermatslasttheorem.blogspot.com/2005/06/division-algorithm-for-gaussian.html
        """
        pass

    def __mul__(self, other):
        """ Multiplies two complex numbers (a + bi)(c + di) = 
        ac + cbi + adi + bdi^2 = (ac - bd) + (cb + ad)i"""
        real = self.a * other.a - self.b * other.b
        imaginary = self.a * other.b + self.b * other.a
        return GaussianIntegerRepresentation(real, imaginary)

    def __mod__(self, other):
        new_value = self.a%other.a
        return IntegerRepresentation(new_value)

    def __sub__(self, other):
        new_value = self.a-other.a
        return IntegerRepresentation(new_value)
    
    def __add__(self, other):
        new_value = self.a+other.a
        return IntegerRepresentation(new_value)

    def is_zero(self) -> bool:
        if self.a == 0:
            return True

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

    def conjugate(self):
        return GaussianIntegerRepresentation(self.a, -self.b)

    def norm(self):
        conjugate = self.conjugate()
        return sqrt((self*conjugate).a)

class EisensteinIntegerRepresentation(DivisibleObject):
    def __init__(self, a: int, b: int):
        # Represents the real part of the number
        self.a = a
        # Represents the imaginary part of the number
        self.b = b

    def __truediv__(self, other):
        pass

    def __mod__(self, other):
        pass
    