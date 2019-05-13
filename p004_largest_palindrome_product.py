import time

def lpp(digits):
    max = 10**digits
    n_1, n_2, num = 0, 0, 0
    for fac_1 in reversed(range(1, max)):
        for fac_2 in reversed(range(1, max)):
            res = fac_1 * fac_2
            if res > num and res == int(str(res)[::-1]):
                n_1, n_2, num  = fac_1, fac_2, res
    return "Palyndrome: {0}x{1} = {2}".format(n_1, n_2, num)

def main():
    start = time.clock()
    print(lpp(3))
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()