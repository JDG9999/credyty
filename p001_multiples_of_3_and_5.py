import time

def multiples(max, numbers):
    sum = 0
    for number in numbers:
        multiple = number
        while multiple < max:
            sum += multiple
            multiple += number
    return "The sum is {0}".format(sum)

def main():
    start = time.clock()
    print(multiples(1000, [3, 5]))
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()