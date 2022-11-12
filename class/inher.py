class Person:
   def __init__(self):
      print("person class __INIT__ function")

   def get_info(self,name , l_name ,age , address , email):
      self.name=name
      self.l_name=l_name
      self.age=age
      self.address = address
      self.email = email

   def show_info(self):
      print(f" name : {self.name} , l_name : {self.l_name} , age : {self.age}, address : {self.address} , email : {self.email}")


# ++++++++++++++++ player class +++++++++++++++++
class Player(Person):
   def __init__(self):
      print("player class __INIT__ function ")


   def team_info(self , team , couch):
      self.team=team
      self.couch= couch

   def show_team_info(self):
      print(f"team is : {self.team}  , couch is : {self.couch}")


# ++++++++++++++++ employee class +++++++++++++++++
class Employee(Person):
   def __init__(self):
      print("employee class __INIT__ function ")

   def get_emp_info(self , father_name , phone , department):
      self.father_name = father_name 
      self.phone = phone 
      self.department = department

   def show_emp_info(self):
      print(f"emp father name : {self.father_name}")
      print(f"emp phone {self.phone} , emp department {self.department} ")



# accessing person class method via employee class obj
print("_______________ emp class object _________________")
obj2 = Employee()
obj2.get_emp_info("ghulam farooq" , "0728151500" , "HR")
obj2.get_info("abdul saboor " , "hemat " , 22 , "kabul " , "abdulsaboorhemat245")
obj2.show_info()
obj2.show_emp_info()

print("_______________ player class object _________________")
# accessing person class methods via player class object 
obj1 = Player()

obj1.get_info("saboor " , "hemat " , 22 , "kabul " , "saboorhemat4600")
obj1.team_info("eleven stars" , "saboor hemat ")


obj1.show_team_info()
obj1.show_info()


