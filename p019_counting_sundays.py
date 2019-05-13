import time
from datetime import date

def starts_sunday(start_date, end_date):
    total = 0
    if (start_date.day == 1):
        check_date = start_date
    else:
        check_date = start_date.replace(month=start_date.month+1)
        check_date = start_date.replace(day=1)
    while check_date < end_date:
        for check_month in range(1, 13):
            check_date = check_date.replace(month=check_month)
            # print(check_date)
            if (check_date.isoweekday() == 6):
                total += 1
        check_date = check_date.replace(year=check_date.year+1)
    solution = "Months starting on a sunday between " + \
            "{0} and {1} is {2}".format(start_date, end_date, total)
    return solution

def main():
    start = time.clock()
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)
    print(starts_sunday(start_date, end_date))
    end = time.clock()
    exec_time = end - start
    print("{0}s execution time".format(exec_time))

if __name__ == "__main__":
    main()