def switch(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))


def choose(argument):
    switcher = {
        "a": "Rectangle()",
        "b": "Square()",
        "c": "Triangle()",
        "d": "Diamond()"
    }
    print(switcher.get(argument, "Invalid shape"))


print("Press a to print... , b to print... , c to print... , d to print...")
choose(str(input("Please input: ")))
