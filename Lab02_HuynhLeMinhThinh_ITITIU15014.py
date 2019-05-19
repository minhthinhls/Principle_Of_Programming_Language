# Huỳnh Lê Minh Thịnh
# ITITIU15014

# Import complex math module
import cmath


# Solve the quadratic equation ax**2 + bx + c = 0
def solve(a, b, c):
    # Calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # Find two roots
    root1 = (-b - cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)

    return [root1, root2]


def ver1():
    # To take coefficient input from the users
    try:
        a = float(input('Enter a: '))
        while a == 0:
            a = float(input("Please input a different from 0: "))
        b = float(input('Enter b: '))
        c = float(input('Enter c: '))

        solution = solve(a, b, c)
        print('The solutions are {0} and {1}'.format(solution[0], solution[1]))
        print("-> Exit function successfully !")
    except ValueError:
        print("Value Error, please input a, b, c as a number !")
        ver1()
    finally:
        pass


def ver2():
    # To take coefficient input from the users
    try:
        # string = "10x^2 + 2x - 5"
        # string = "10*x^2 + 2*x - 5 = 0"
        string = input("Please input your equation as format (a*x^2 + b*x + c) or (a*x^2 + b*x + c = 0): ")
        string = string.replace(" ", "")  # Reduce all gap in the expression
        string = string.replace("x^2", " ").replace("x", " ").replace("*", "").replace("=0", "")
        # array = [int(s) for s in re.findall('\\d+', string)]
        array = string.split(" ")
        solution = solve(float(array[0]), float(array[1]), float(array[2]))
        print('The solutions are {0} and {1}'.format(solution[0], solution[1]))
        print("-> Exit function successfully !")
    except ValueError:
        print("Value Error, please input a, b, c as a number !")
        ver2()
    finally:
        pass


def calculator():
    # expression = "2 * 2 * 100 + ( 5 * 4 + 1 ) / 3"
    # expression = "Please input your expression: "
    try:
        expression = input("Please input your expression: ")
        print(eval(expression))
        print("-> Exit function successfully !")
    except (SyntaxError, NameError, TypeError):
        print("Syntax Error! Please write the expression again !")
        calculator()
    except ZeroDivisionError:
        print("Cannot divide by zero! Please write the expression again !")
        calculator()
    finally:
        pass


ver1()
ver2()
calculator()
