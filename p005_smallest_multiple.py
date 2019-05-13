import time

def small_multiple(max):
    num = max
    while True:
        evenly_div = True
        for v in range(2, max+1):
            if num % v != 0:
                evenly_div = False
                break
        if (evenly_div):
            return "Smallest number multiple of all numbers up until {0} is {1}".format(max,num)
        num += max

def small_multiple_2(max):
    num = max
    while True:
        divs = [num % i for i in range(2,max+1)]
        if sum(divs) > 0:
            num += max
        else:
            return "Smallest number multiple of all numbers up until {0} is {1}".format(max,num)
    
def main():
    start = time.clock()
    print(small_multiple(20))
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()