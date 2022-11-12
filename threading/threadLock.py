# A race condition occurs when two threads try to access a shared variable simultaneously.
from threading import Thread, Lock
from time import sleep


counter = 0


def increase(by, lock):
    global counter
   # if we commint the lock the output is 20  if there is lock the output is 30
    lock.acquire()

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}')

    lock.release()


lock = Lock()

t1 = Thread(target=increase, args=(10, lock))
t2 = Thread(target=increase, args=(20, lock))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'The final counter is {counter}')