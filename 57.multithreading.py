#MULTITHEADING:is a technique in programming that allows multiple threads of execution to 
#run concurrently within a single process.in python,we can use the threading module to 
#implement mutlithreading.we can use thrading by importing the threading module.
import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")#indicates some task being done
    time.sleep(seconds)
    return seconds

time1=time.perf_counter()
# func(4)
# func(2)                                   #normal code
# func(3)
# time2=time.perf_counter()
# print(time2-time1)                          #complete time 
# print("_________________________________________________________________________________")

#to create a thread we need to create thread object and then call its start() method.

t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])   #same code using thread
t3=threading.Thread(target=func,args=[3])

t1.start()
t2.start()
t3.start()
time4=time.perf_counter()
print(time4-time1)                          

#the start() method runs the thread and then to stop the execution,we use the join method.
t1.join()
t2.join()
t3.join()
time5=time.perf_counter()
print(time5-time1)                          #complete time
print("_________________________________________________________________________________")

from concurrent.futures import ThreadPoolExecutor

def poolingDemo():
    with ThreadPoolExecutor() as executer:
        future1=executer.submit(func,4)
        future2=executer.submit(func,2)
        future3=executer.submit(func,3)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        print("_________________________________________________________________________________")

        l=[4,2,3]
        results=executer.map(func,l)
        for result in results:
            print(result)
poolingDemo()