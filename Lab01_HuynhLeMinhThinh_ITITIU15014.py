# Huỳnh Lê Minh Thịnh
# ITITIU15014


def calculator():
    x = float(input("Please input x: "))
    operator = input("Please choose your operator (+, -, *, /): ")
    while not ["+", "-", "*", "/"].__contains__(operator):
        operator = input("Please choose your operator again (+, -, *, /): ")
    y = float(input("Please input y: "))
    while operator == '/' and y == 0:
        y = float(input("Please input y different from 0: "))
    if operator == '+':
        print("The sum is: " + str(x + y))
        return
    elif operator == '-':
        print("The minus is: " + str(x - y))
        return
    elif operator == '*':
        print("The multiplication is: " + str(x * y))
        return
    elif operator == '/':
        print("The division is: " + str(x / y))
        return
    raise SyntaxError("Your operator is not handled !")


class Shape:
    def __init__(self, hollow, thickness):
        self.hollow = hollow
        self.thickness = thickness

    def print(self):
        return


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


class Square(Rectangle):
    def __init__(self, hollow, thickness, size):
        Shape.__init__(self, hollow, thickness)
        self.height = size
        self.width = size


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
        countdown = int(self.height / 2 - 0.5)
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


calculator()
Rectangle(True, 2, 5, 10).print()  # hollow = True, thickness = 2, height = 5, width = 10
Square(True, 3, 5).print()  # hollow = True, thickness = 3, height = 5
Triangle(True, 2, 6).print()  # hollow = True, thickness = 2, height = 6
Diamond(True, 3, 9).print()  # hollow = True, thickness = 3, height = 9
