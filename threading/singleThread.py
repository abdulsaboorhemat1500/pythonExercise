from time import sleep, perf_counter 
'''  sleep function is to sleep a process for sec on that time the process is switching to another 
process   and perf_counter is for  getting the exact time  we use that to get the execution time of the process '''

def task():
    print('Starting a task...')
    sleep(1)
    print('done')

start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

''' If we call the task() function 10 times, it would take about 10 seconds to complete.'''