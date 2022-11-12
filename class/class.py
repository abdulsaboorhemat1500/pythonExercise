class greating:
   country="afghanistan"

   def __init__(self, name , age, id , address):
      self.name = name
      self.age = age 
      self.id = id 
      self.address = address
      
   def get_info(self , faculty , semester , rollnum):
      self.faculty= faculty
      self.semester= semester
      self.rollnum= rollnum

   def say_hi(self):
      print(f"hello {self.name} how are you, your age is {self.age} and your id number is {self.id}  and your address is {self.address} ")
      print(self.country)

   def show_info(self):
      print(f"faculty : {self.faculty} , semester : {self.semester} , rollnum : {self.rollnum}")


obj = greating("saboor " , 22,349, "kabul/Chahar rahi qambar (Afghanistan)")
obj.say_hi()
obj.get_info("cs" , 2 , "?")
obj.show_info()