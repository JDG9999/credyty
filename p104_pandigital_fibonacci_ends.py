import time

def fibonacci_pandigital():
    a = 1
    b = 1
    num = 2
    k = 3
    while True:
        a, b = b, num
        num = a + b
        k = k + 1
        # print("Testing k=" + str(k))
        starts_pandigital = is_pandigital(str(num)[:9])
        if (starts_pandigital):
            ends_pandigital = is_pandigital(str(num)[-9:])
            if (ends_pandigital):
                solution = "k={0}, number={1}".format(k, num)
                return solution
        # if (k % 10000 == 0):
        #     print("k=" + str(k))
        # if (k > 500000):
        #     return "*Error*"

def is_pandigital(num):
    return not '123456789'.strip(num)

def main():
    start = time.clock()
    print(fibonacci_pandigital())
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()