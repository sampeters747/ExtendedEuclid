
# Extended Euclidean Algorithm
This program implements the extended euclidean algorithm for the integers Z, gaussian integers Z[i] and eisenstein integers Z[w].

The actual algorithm implementation is pretty standard, running through the same steps you'd find in your favorite abstract algebra textbook, which explains it better than I can. For that reason I'm going to skip covering the basic algorithm itself, and instead mainly talk about the more challenging parts of the project.

## Implementing a General Version of the Algorithm
The euclidean algorithm isn't limited to the domain of integers, it works in fundamentally the same way with any euclidean domain. 

Euclidean domains are integral domains that allow some form of devision between two elements a, b in the domain so that a = q*b + r, with q and r being in the same domain.

In order for my program to reflect that, I used Python classes to represent each type of integer and abstracted away the domain specific operations into class methods (specifically magic methods). That way, the euclidean algorithm function works without ever explicitly checking what type of object it's been given. Instead, I relied on defining division and multiplication as class methods so that when I write x//y inside the euclidean algorithm function, Python will automatically know which division algorithm to use, and I won't have to include code specific to whatever type of integer a and b are inside the euclidean algorithm function.

This has several advantages:
* Extendability: By moving all the domain specific logic into class methods, someone can extend this program to work with another type of euclidean domain just by creating a new class with the required devision, multiplication, subtraction, and addition methods.
* Readability: Abstracting away the division algorithms to class methods makes the algorithm function much more readable. For example, the division algorithm for gaussian integers is nearly 20 lines, including that in the main algorithm function would double the length of it, making it much harder to understand the parts that matter.
* Testability: Creating a general function instead of separate implementations for each type allowed me to verify the algorithm is working correctly using simple integers, and be confident that this translates to it also working for eisenstein integers which are much harder to test on their own.

## Efficiency Tweaks
Note: I found the mathematical reasoning that makes this part possible here: https://brilliant.org/wiki/extended-euclidean-algorithm/ .

In the normal extended euclidean algorithm, once you've finished computing the gcd you retrace your steps, using the previous quotients and remainders leftover from applying the division algorithm multiple times in order to compute the Bezout's coefficients of a and b, which are two numbers s and t that satisfy the expression 
s*a + t*b = gcd(a,b).

This works, but adds some unneccesary iteration and complexity when translated to code because it's possible to compute s and t at the same time you're computing the gcd.

To do this we rely on two expressions

## Usage
For an interactive demo, run the interactive.py file. Note: When entering gaussian integers, they must always be of the form x+yi or x-yi. Ex. 5+0i, 0-6i, 6 + 7i, 10-20i, etc. The same goes for eisenstein numbers numbers, which must be either in the form x+yw or x-yw, where x and y are integers.

## Testing
Assuming you have python3 installed, you run automated tests of this code by navigating to this folder in your favorite terminal/commandline, and running the command:  
`python3 tests.py --verbose`  
This normally should take 0-5 seconds to run, and at most 10 seconds. All test cases are stored in the tests.py file. 

## Definitions Z, Z[i], Z[omega] and their representations in Python
Talks about how all 3 were represented in Python, with emphasis on them all inheriting div/mod operations.

## Misc.
Not sure what else quite yet.