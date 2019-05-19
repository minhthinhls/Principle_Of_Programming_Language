# Huỳnh Lê Minh Thịnh
# ITITIU15014

# Import complex math module
import cmath
import re


# Create an abstract class, namely: Shape.
class Shape:
    def __init__(self, hollow, thickness):
        self.hollow = hollow
        self.thickness = thickness

    def print(self):
        return


# Implement Rectangle class from Shape.
class Rectangle(Shape):
    def __init__(self, hollow, thickness, height, width):
        Shape.__init__(self, hollow, thickness)
        self.height = height
        self.width = width

    def print(self):
        print("*The " + str(self.__class__.__name__) + ": ")
        for i in range(self.height * self.thickness):
            x = ""
            for j in range(self.width * self.thickness):
                if (self.hollow and self.thickness - 1 < i < self.height * self.thickness - self.thickness
                        and self.thickness - 1 < j < self.width * self.thickness - self.thickness):
                    x += "  "
                else:
                    x += "* "
            print("    " + x)


# Inherit Square class from Rectangle class.
class Square(Rectangle):
    def __init__(self, hollow, thickness, size):
        Shape.__init__(self, hollow, thickness)
        self.height = size
        self.width = size


# Implement Triangle class from Shape.
class Triangle(Shape):
    def __init__(self, hollow, thickness, height):
        Shape.__init__(self, hollow, thickness)
        self.height = height

    def print(self):
        print("*The Triangle: ")
        self.height *= self.thickness
        k = 2 * self.height - 2
        for i in range(0, self.height):
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i + 1):
                if (self.hollow and self.thickness - 1 < i < self.height - self.thickness
                        and self.thickness - 1 < j < i - self.thickness + 1):
                    print("  ", end="")
                else:
                    print("* ", end="")
            print("\r")


# Implement Diamond class from Rectangle class.
class Diamond(Triangle):
    def __init__(self, hollow, thickness, height):
        Triangle.__init__(self, hollow, thickness, height)

    def print(self):
        print("*The Diamond: ")
        self.height *= self.thickness
        k = self.height
        for i in range(0, int(self.height / 2)):
            for j in range(0, k):
                print(end=" ")
            k -= 1
            for j in range(0, i + 1):
                if (self.hollow and self.thickness - 1 < i < self.height - self.thickness
                        and self.thickness - 1 < j < i - self.thickness + 1):
                    print("  ", end="")
                else:
                    print("* ", end="")
            print("\r")
        if self.height % 2 == 0:
            k += 1
        countdown = int(self.height / 2)
        for i in range(int(self.height / 2), self.height):
            for j in range(0, k):
                print(end=" ")
            k += 1
            for j in range(0, self.height - i):
                if (self.hollow and self.thickness - 1 < i < self.height - self.thickness
                        and self.thickness - 1 < j < countdown - self.thickness + 1):
                    print("  ", end="")
                else:
                    print("* ", end="")
            countdown -= 1
            print("\r")


# Create an implemented class, namely: QuadraticEquation. With a, b, c are null values.
class QuadraticEquation:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.root1 = None
        self.root2 = None

    # Solve the quadratic equation ax**2 + bx + c = 0
    def solve(self):
        try:
            # Calculate the discriminant
            d = (self.b ** 2) - (4 * self.a * self.c)

            # Find two roots
            self.root1 = (-self.b - cmath.sqrt(d)) / (2 * self.a)
            self.root2 = (-self.b + cmath.sqrt(d)) / (2 * self.a)
        except TypeError:
            print("Please first run input() before solve() !")
            self.input().solve()
        finally:
            return self

    # Input values from the console.
    def input(self):
        # To take coefficient input from the users
        try:
            self.a = float(input('Enter a: '))
            while self.a == 0:
                self.a = float(input("Please input a different from 0: "))
            self.b = float(input('Enter b: '))
            self.c = float(input('Enter c: '))
        except ValueError:
            print("Value Error, please input a, b, c as a number !")
            self.input()
        finally:
            return self

    def solution(self):
        if self.root1 is None:
            self.input().solve()
        print('The solutions are {0} and {1}'.format(self.root1, self.root2))
        print("-> Exit function successfully !")


# Inherit QuadraticEquationExpression() class from QuadraticEquation() class.
class QuadraticEquationExpression(QuadraticEquation):
    def __init__(self):
        QuadraticEquation.__init__(self)
        self.pattern = "^(\-?\d*)\*?x\^2([\+|\-]\d*)\*?x([\+|\-]\d+)?(\=0)?$"

    # Overriding input method from QuadraticEquation() class
    def input(self):
        # Used for mapping coefficient groups (a, b, c) into correct values, using Lambda Expression. Line 180 !
        def mapping(x):
            if x == '':
                return '1'
            elif x == '-':
                return '-1'
            elif x == '+':
                return '1'
            else:
                return x

        try:
            string = input("*Please input your equation as formats below: \n" +
                           "(a*x^2 + b*x + c) or (a*x^2 + b*x + c = 0) or " +
                           "(ax^2 + bx + c) or (ax^2 + bx + c = 0) or \n" +
                           "(x^2 + x + c) or (x^2 + x + c = 0) or " +
                           "(x^2 + x) or (x^2 + x = 0): \n")
            string = string.replace(" ", "")  # Reduce all gap in the expression
            match = re.search(self.pattern, string)
            if match:
                groups = list(map(lambda x: mapping(x), match.groups()))
                self.a = float(groups.__getitem__(0))
                if self.a == 0:
                    raise ZeroDivisionError
                self.b = float(groups.__getitem__(1))
                if match.groups().__getitem__(2) is None:  # If c does not exist in the expression, then c = 0
                    self.c = 0
                else:  # Else get c from matching groups, at groups.index(2)
                    self.c = float(groups.__getitem__(2))
                print("*Respectively A, B, C are: [" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + "]")
            else:
                raise TypeError

        except ValueError:
            print("Value Error, please input a, b, c as a number !")
            self.input()
        except TypeError:
            print("Type Error, please input the equation as standard formats !")
            self.input()
        except ZeroDivisionError:
            print("Zero Division Error, please input a different from 0 !")
            self.input()
        finally:
            return self


class Calculator:
    def __init__(self):
        self.expression = None
        self.result = None

    # Input expression from the console.
    def input(self):
        try:
            self.expression = input("Please input your expression: ")
        except EOFError:
            print("End of File Error, please input again !")
            self.input()
        finally:
            return self

    # Evaluating the expression.
    def evaluate(self):
        try:
            self.result = eval(self.expression)
        except (SyntaxError, NameError, TypeError):
            print("Syntax Error! Please write the expression again !")
            self.input().evaluate()
        except ZeroDivisionError:
            print("Cannot divide by zero! Please write the expression again !")
            self.input().evaluate()
        finally:
            return self

    def solution(self):
        if self.result is None:
            self.input().evaluate()
        print("The result is: " + str(self.result))
        print("-> Exit function successfully !")


Rectangle(True, 2, 5, 10).print()  # hollow = True, thickness = 2, height = 5, width = 10
Square(True, 3, 5).print()  # hollow = True, thickness = 3, height = 5
Triangle(True, 2, 6).print()  # hollow = True, thickness = 2, height = 6
Diamond(True, 3, 9).print()  # hollow = True, thickness = 3, height = 9
QuadraticEquation().input().solve().solution()
QuadraticEquationExpression().input().solve().solution()
Calculator().input().evaluate().solution()
