import time

def get_passcode():
    digits = {}
    file = open('p079_keylog.txt', 'r')
    # get the digits in the fragments
    for line in file:
        line = line.strip('\n')
        for i, digit in enumerate(line):
            if int(digit) not in digits:
                digits[int(digit)] = set()
            for trailing_digit in line[i+1:]:
                digits[int(digit)].add(int(trailing_digit))
    # print(digits)
    # order according to size
    passcode = ''
    while len(digits) > 0: 
        biggest_set = -1
        value = None
        for digit in digits:
            if len(digits[digit]) > biggest_set:
                biggest_set = len(digits[digit])
                value = digit
        passcode += str(value)
        del digits[value]
    solution = "The passcode is : {0}".format(passcode)
    return solution
        
def main():
    start = time.clock()
    print(get_passcode())
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))
    
if __name__ == "__main__":
    main()