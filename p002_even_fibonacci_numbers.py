import time

def even_fib(max):
    sum = 2
    prev_1 = 1
    prev_2 = 2
    num = 3
    while num < max:
        prev_1, prev_2 = prev_2, num
        num = prev_1 + prev_2
        if (num % 2 == 0):
            sum += num
    return "The sum is {0}".format(sum)

def main():
    start = time.clock()
    print(even_fib(4*10**6))
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()