class Animal:
     def __init__(self, name):
          self.name = name
          
     def info(self):
          print("Animal name : ", self.name)
          
class Dog(Animal):
     def __init__(self, name, breed):
          super().__init__(name)
          self.breed = breed
          
     def detail(self):
          print(self.name, "is a", self.breed)
          
d = Dog("Buddy", "golden dog")
d.info()
d.detail()