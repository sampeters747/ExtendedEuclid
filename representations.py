""" Classes that represent Z, Z[i], Z[omega]. Includes base parent class DivisibleObject that requires
floordiv and mod methods be implemented. """

# Base object
class DivisibleObject:
    # Requires that floordiv method be defined in any class that inherits from this class
    def __floordiv__(self, other):
        raise NotImplementedError()

    # Requires that mod method be defined in any class that inherits from this class
    def __mod__(self, other):
        raise NotImplementedError()

    # Requires that any subclass implements an is_zero() method to check if the object is the zero element
    def is_zero(self) -> bool:
        raise NotImplementedError()

class IntegerRepresentation(DivisibleObject):
    def __init__(self, a: int):
        # Holds value of integer
        self.a = a

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass


class GaussianIntegerRepresentation(DivisibleObject):
    def __init__(self, a: int, b: int):
        # Represents the real part of the number
        self.a = a
        # Represents the imaginary part of the number
        self.b = b

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

class EisensteinIntegerRepresentation(DivisibleObject):
    def __init__(self, a: int, b: int):
        # Represents the real part of the number
        self.a = a
        # Represents the imaginary part of the number
        self.b = b

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass
    