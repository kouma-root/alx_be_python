""" try :
    number1 = int(input("Enter the first number"))
    number2 = int(input("Enter the second number"))
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("You can divided by Zero")

try :
    file_p = open("file.txt", "r")
except FileNotFoundError :
    print("File Not Found, Please check the file in your Directories")
else:
    file_p.close()
    print("Program closed")
   """  

class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number
    
    def __str__(self):
        return (f"The Value {self.number} is Too Hight, Expected Value under 100")

def add_value(value) :
    if value > 100 : 
        raise ValueTooHighError(value)
    else :
        print(f"Your Value is {value}")
        


number = int(input("Enter a number :"))
try :
    add_value(number)
except ValueTooHighError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")