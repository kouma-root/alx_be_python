#Oriented-Object Programming test
class Student :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Student_info(self) :
        return f"Name: {self.name}, Age: {self.age}"
    
class Product :
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def Product_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    def total_value(self):
        return self.price * self.quantity
    
Student1 = Student("Alice", 20)
Product1 = Product("Laptop", 1000, 5)
print(Student1.Student_info())
print(Product1.Product_info())
print(f"Total value of {Product1.name}: {Product1.total_value()}")