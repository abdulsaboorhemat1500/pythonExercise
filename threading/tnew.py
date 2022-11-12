from threading import Thread
from time import sleep

class array:
   def __init__(self ,arr):
      self.array=arr
      sleep(1)

   def sum(self ,arr):
      res=0
      for i in arr:
         res=res+i
         sleep(1)
      print(res)

   
   def revers(self , arr):
      for i in range(0, len(arr)):    
         for j in range(i+1, len(arr)):    
            if(arr[i] > arr[j]):    
                  temp = arr[i];    
                  arr[i] = arr[j];    
                  arr[j] = temp;
         sleep(1)
      print(arr)


a=[1,3,4,2,5,10,6,9,8]
obj=array(a)

t1=Thread(target=obj.sum , args=(a,)  )
t2=Thread(target=obj.revers , args=(a,) )

t1.start()
t2.start()

t1.join()
t2.join()

print("end of program")