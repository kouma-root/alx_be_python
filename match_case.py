print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

expression = int(input("Choose an option : "))

match expression:
    case 1:
        print("Addition")
    case 2:
        print("Subtraction")
    case 3:
        print("Multiplication")
    case 4:
        print("Division")
    case _:
        print("Invalid option")
# This code snippet demonstrates the use of match-case for a simple calculator menu.