import time
import math

def lpf(num):
    div = num
    for div in reversed(range(1, num+1)):
        if is_prime(div) and is_factor(div, num):
            return "The lpf is {0}".format(div)

def is_prime(num):
    pos = 3
    mod = 1
    if num % 2 == 0:
        return False
    else:
        mod = 2
    while pos <= int(math.sqrt(num)):
        if num % pos == 0:
            return False
        pos += mod
    return True

def is_factor(div, num):
    return num % div == 0

def lpf_arithmetic(num):
    new_num = num
    largest_factor = 1
    div = 2
    while new_num != 1:
        if (new_num % div == 0):
            new_num = new_num / div
            largest_factor = div
        else:
            div += 1
    return "The lpf is {0}".format(largest_factor)

def main():
    start = time.clock()
    print(lpf_arithmetic(600851475143))
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()