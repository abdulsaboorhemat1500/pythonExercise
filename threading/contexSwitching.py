import threading  
import time

def print_hello(): 
  for i in range(20):
    if i == 10:
      time.sleep(2)   # in 11th iteration it sleep and the other process take action
    print("Hello")


def print_numbers(num): 
  for i in range(num+1):
    print(i)


print("Greetings from the main thread.")
thread1 = threading.Thread(target = print_hello, args = ())
thread2 = threading.Thread(target = print_numbers, args = (10,))  

thread1.start() 
thread2.start() 
thread1.join()
thread2.join()

print("It's the main thread again!")
print("Threads 1 and 2 have finished executing.")