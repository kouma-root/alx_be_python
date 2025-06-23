class Book :
    count_book = 0
    
    def __init__(self, name) -> None:
        self.name = name
        Book.count_book +=1
    @classmethod    
    def display_count(cls):
        return f"{cls.count_book} is the number of book"
    
    
b1 = Book("Riri")
b2 = Book("Rara")

print(Book.count_book)


class Calculator :
    def __init__(self, number_1, number_2) -> None:
        self.number_1 = number_1
        self.number_2 = number_2
    @staticmethod
    def add(number_1, number_2):
        return number_1 + number_2
    
    @staticmethod
    def multiply(number_1, number_2):
        return number_1 * number_2    
    
    
cal = Calculator(12, 4)

print(Calculator.add(12,4))
print(Calculator.multiply(6,5))

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f"You are {self.name}, and you are {self.age} year old"
        
    @classmethod
    def creat_child(cls, age):
       cls.age = 0
        
pers = Person("Kouma",22)
print(pers)
pers1=Person("bebe",Person.creat_child)
print(pers1)