import time

def triplet(sum):
    for a in range(1, sum):
        for b in range((a+1), sum):
            c = (a**2 + b**2)**(0.5)
            if a+b+c == sum:
                product = a*b*c
                solution = "a={0}, b={1}, c={2}, product={3}".format(a,b,c,product)
                return solution
    return "There's no solution"

def main():
    start = time.clock()
    print(triplet(1000))
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()