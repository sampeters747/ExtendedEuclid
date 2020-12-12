from algorithm import *
from representations import *
import re

eisensteinPattern = re.compile(r"^(?P<a>\d+)\s*(?P<operator>[\+\-])\s*(?P<b>\-?\d+)w\s*")
gaussianPattern = re.compile(r"^(?P<a>[\+\-]?\d+)\s*(?P<operator>[\+\-])\s*(?P<b>\-?\d+)i\s*")



def main():
    print("This interactive program lets you enter your own values and run the extended euclidean algorithm on them.")
    mode = 0
    while True:
        if mode == 0:
            print("Choose the mode by entering integer, gaussian, eisenstein or q to quit")
            user_input = input("Mode: ")
            if user_input == "integer":
                mode = 1
            elif user_input == "gaussian":
                mode = 2
            elif user_input == "eisenstein":
                mode = 3
            elif user_input == "q":
                break
            else:
                print("Sorry, that mode does not exist.")
            print()
        elif mode == 1:
            user_input = input("Enter the first integer, or q to go back to the mode selection menu: ")
            if user_input == "q":
                mode = 0
                print("")
                continue
            try:
                a = int(user_input)
            except:
                print("Couldn't understand this input, is it an integer?")
                continue
            user_input = input("Second integer: ")
            try:
                b = int(user_input)
            except:
                print("Couldn't understand this input, is it an integer?")
                continue
            try:
                my_gcd, t, s = extendedEuclidAlgorithm(IntegerRepresentation(a), IntegerRepresentation(b))
                print(f"gcd({a}, {b}) = {my_gcd}")
                print(f"Bezout's coefficients are {t} and {s}, so {t}*{a} + {s}*{b} = {my_gcd}")
            except:
                print("Something went wrong while trying to compute the gcd, restarting")
            print()

        elif mode == 2:
            user_input = input("Enter the first gaussian integer, or q to go back to the mode selection menu: ")
            if user_input == "q":
                mode = 0
                print("")
                continue
            
            match = gaussianPattern.match(user_input)
            if match:
                real = int(match.groupdict()['a'])
                imaginary = int(match.groupdict()['b'])
                if match.groupdict()['operator'] == "-":
                    imaginary *= -1
                a = GaussianIntegerRepresentation(real, imaginary)
            else:
                print("Couldn't understand this input, is it a gaussian integer?")
                continue
            user_input = input("Second gaussian integer: ")
            match = gaussianPattern.match(user_input)
            if match:
                real = int(match.groupdict()['a'])
                imaginary = int(match.groupdict()['b'])
                if match.groupdict()['operator'] == "-":
                    imaginary *= -1
                b = GaussianIntegerRepresentation(real, imaginary)
            else:
                print("Couldn't understand this input, is it a gaussian integer?")
                continue

            try:
                my_gcd, t, s = extendedEuclidAlgorithm(a, b)
                print(f"gcd({a}, {b}) = {my_gcd}")
                print(f"Bezout's coefficients are {t} and {s},\n({t})*({a}) + ({s})*({b}) = {my_gcd}")
            except:
                print("Something went wrong while trying to compute the gcd, restarting")
            print()

        elif mode == 3:
            user_input = input("Enter the first eisenstein integer, or q to go back to the mode selection menu: ")
            if user_input == "q":
                mode = 0
                print("")
                continue
            
            match = eisensteinPattern.match(user_input)
            if match:
                real = int(match.groupdict()['a'])
                imaginary = int(match.groupdict()['b'])
                if match.groupdict()['operator'] == "-":
                    imaginary *= -1
                a = EisensteinIntegerRepresentation(real, imaginary)
            else:
                print("Couldn't understand this input, is it a eisenstein integer?")
                continue
            user_input = input("Second eisenstein integer: ")
            match = eisensteinPattern.match(user_input)
            if match:
                real = int(match.groupdict()['a'])
                imaginary = int(match.groupdict()['b'])
                if match.groupdict()['operator'] == "-":
                    imaginary *= -1
                b = EisensteinIntegerRepresentation(real, imaginary)
            else:
                print("Couldn't understand this input, is it a eisenstein integer?")
                continue
            try:
                my_gcd, t, s = extendedEuclidAlgorithm(a, b)
                print(f"gcd({a}, {b}) = {my_gcd}")
                print(f"Bezout's coefficients are {t} and {s},\n({t})*({a}) + ({s})*({b}) = {my_gcd}")
            except:
                print("Something went wrong while trying to compute the gcd, restarting")
            print()


main()

    