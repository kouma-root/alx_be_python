
class Animal :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sleep(self):
        return(f"{self.name} is sleeping")
    
    def eat(self):
        return(f"{self.name} like to eat many things")
        
        
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def bark(self):
        return(f"Woof")
        
    def eat(self):
        return(f"{self.name} like to eat good meat")
      

anim = Animal("Chiken",2)
print(anim.eat())
print(anim.sleep())
dog = Dog("Milou",12)
print(dog.eat())
print(dog.sleep())
print(dog.bark())