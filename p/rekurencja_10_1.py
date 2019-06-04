import time

def find_fib_num(num):
    if num == 1 or num == 2:
        return 1
    else:
        find_fib_num(num -2) + find_fib_num (num -1)

def loop_fib(num):
    a, b= 0, 1
    for elem in range(num):
        a,b = b, a+b
        return a


start= time.procces_time()
print(find_fib_num(50))
stop= time.procces_time()
print('f czas wynosi {stop - start}')

start1= time.procces_time()
print(loop_fib(50))
stop1= time.procces_time()
print('f czas wynosi {stop - start}')
