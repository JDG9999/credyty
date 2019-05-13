import time

def pascal(limit, div):
    total = 1
    prev_row = [1]
    for row_number in range(2, (limit+1)):
        row = [1 for i in range(row_number)]
        total += 2
        for i, _ in enumerate(row[1:-1]):
            row[i+1] = prev_row[i+1] + prev_row[i]
            if (row[i+1] % div != 0):
                total += 1
        prev_row = row
        # if (row_number % 100000 == 0):
        #     print(str(row_number))
        solution = "Elements in the triangle not divisible by {0} " + \
                    "in the first {1} levels is {2}".format(div, limit, total)
    return solution           

def main():
    start = time.clock()
    print(pascal(100, 7))
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()