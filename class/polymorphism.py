class Person:
   def __init__(self):
      print("person class __INIT__")

   def say_hi(self , name):
      self.name = name 
      print(f"welcome  : {self.name}")

class Employee(Person):
   def __init__(self):
      print("Employee class __INIT__ ")

   def say_hi(self , name ):
      self.name = name 

      print(f" hello dear  friend  : {self.name}")


obj1 = Person()
obj2 = Employee()

obj1.say_hi("saboor")
obj2.say_hi("kaihan")
