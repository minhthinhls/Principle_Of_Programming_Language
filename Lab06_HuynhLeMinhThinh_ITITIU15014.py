# Huỳnh Lê Minh Thịnh
# ITITIU15014
import math


class Shape:
    def __init__(self, hollow, thickness):
        self.hollow = hollow
        self.thickness = thickness

    def area(self):
        raise NotImplementedError

    def circumference(self):
        raise NotImplementedError

    def showDetailInfo(self):
        print("%s's area: %s & circumference: %s \n" % (self.__class__.__name__, self.area(), self.circumference()))
        return self

    def print(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, hollow, thickness, height, width):
        Shape.__init__(self, hollow, thickness)
        self.height = height
        self.width = width

    def area(self):
        return (self.height * self.thickness) * (self.width * self.thickness)

    def circumference(self):
        return (self.height * self.thickness + self.width * self.thickness) * 2

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
        return self


class Square(Rectangle):
    def __init__(self, hollow, thickness, size):
        Rectangle.__init__(self, hollow, thickness, size, size)


class Triangle(Shape):
    def __init__(self, hollow, thickness, height):
        Shape.__init__(self, hollow, thickness)
        self.height = height

    def area(self):
        return (self.height * self.thickness) ** 2 / 2

    def circumference(self):
        height = self.height * self.thickness
        return math.sqrt(height ** 2 + (height / 2) ** 2) * 2 + height

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
        return self


class Diamond(Triangle):
    def __init__(self, hollow, thickness, height):
        Triangle.__init__(self, hollow, thickness, height)

    def circumference(self):
        height = self.height * self.thickness
        return math.sqrt((height / 2) ** 2 * 2) * 4

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
        return self


def shapeTypeInput():
    try:
        return str(input("Please enter shapes type you want to implement {rectangle, square, triangle, diamond}: "))
    except (ValueError, SyntaxError, NameError, TypeError):
        return shapeTypeInput()
    finally:
        pass


def valueInput(properties: str):
    try:
        value = int(input("Please enter %s: " % properties))
        if value < 1:
            print("Value must be a positive number !")
            raise ValueError
        return value
    except (ValueError, SyntaxError, NameError, TypeError):
        return valueInput(properties)
    finally:
        pass


def booleanInput(properties: str):
    try:
        bool = str(input("Please enter %s {true, false}: " % properties))
        while not ["true", "false"].__contains__(bool.lower()):
            raise TypeError
        if bool.__eq__("true"):
            return True
        if bool.__eq__("false"):
            return False
    except (ValueError, SyntaxError, NameError, TypeError):
        return booleanInput(properties)
    finally:
        pass


def userInput():
    shapeList = list()
    for i in range(valueInput("number of shapes you want to implement")):
        shapeType = shapeTypeInput().lower()
        while not ["rectangle", "square", "triangle", "diamond"].__contains__(shapeType):
            shapeType = shapeTypeInput().lower()

        if shapeType.__eq__("rectangle"):
            shapeList.append(Rectangle(booleanInput("is Hollow ?"), valueInput("Thickness"), valueInput("Height"),
                                       valueInput("Width")))
        if shapeType.__eq__("square"):
            shapeList.append(Square(booleanInput("is Hollow ?"), valueInput("Thickness"), valueInput("Size")))
        if shapeType.__eq__("triangle"):
            shapeList.append(Triangle(booleanInput("is Hollow ?"), valueInput("Thickness"), valueInput("Height")))
        if shapeType.__eq__("diamond"):
            shapeList.append(Diamond(booleanInput("is Hollow ?"), valueInput("Thickness"), valueInput("Height")))

    return shapeList


# Rectangle(True, 2, 5, 10).print().showDetailInfo()  # hollow = True, thickness = 2, height = 5, width = 10
# Square(True, 3, 5).print().showDetailInfo()  # hollow = True, thickness = 3, size = 5
# Triangle(True, 2, 6).print().showDetailInfo()  # hollow = True, thickness = 2, height = 6
# Diamond(True, 3, 9).print().showDetailInfo()  # hollow = True, thickness = 3, height = 9

def main():
    for shape in userInput():
        shape.print().showDetailInfo()
    pass


if __name__ == "__main__":
    main()
