from threading import *
from time import sleep

class greating:

   def welcome(self ,x):
      for i in range(5):
         print("welcome to : ",x)
         sleep(1)

   def say_name(self , name):
      for i in range(5):
         print("Dear  : ",name )
         sleep(1)

obj = greating()

t1 = Thread(target=obj.say_name ,args=('khalid',))
t2 = Thread(target=obj.welcome, args=('afghanistan',))

t1.start()

t2.start()

print("end of program")
