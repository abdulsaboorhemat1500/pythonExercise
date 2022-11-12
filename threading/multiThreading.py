from time import sleep, perf_counter
from threading import Thread

def task():
    for i in range(5):
        print('hello' ,i)
        sleep(1)
        print("end " , i)
        

start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()      # this thread wait for the second one to complate 

end_time = perf_counter()


print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

''' The Thread() accepts many parameters. 
target: specifies a function (task) to run in the new thread.
args: specifies the arguments of the function (task). 
if there are arguments so then The args argument is a tuple.

and 
The join() method provides a way for one thread to block until another thread has finished'''
