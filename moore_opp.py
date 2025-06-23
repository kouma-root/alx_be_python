class Area:
    def calsulate_area(self):
        pass
    
class Rectangle(Area):
    def __init__(self, L, l):
        self.L = L 
        self.l = L
        
    def calsulate_area(self):
        return self.L*self.l
        
        
        
rect = Rectangle(12,3)
print(rect.calsulate_area())

class Birt:
    def __init__(self,name) -> None:
        self.name = name
        
    def fly(self):
        return f"{self.name} can fly"
    
class Mammal :
    def __init__(self,name) -> None:
        self.name = name
        
    def run(self):
        return f"{self.name} can run"
    
class Bat(Birt,Mammal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
        
        
bat1 = Bat("Riri")
print(bat1.fly())
print(bat1.run())


class Dog:
    def __init__(self) -> None:
        pass
    def make_sound(self):
        return "Sound from Dog"
    
class Cat:
    def __init__(self) -> None:
        pass
    def make_sound(self):
        return "Sound from Cat"
    
class Bird:
    def __init__(self) -> None:
        pass
    def make_sound(self):
        return "Sound from Bird"
    
def let_them_speak( obje):
    print(obje.make_sound())
    
d = Dog()
c = Cat()
b = Bird()

l = [d,c,b]
for o in l :
    let_them_speak(o)
    
