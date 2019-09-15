## Python Regex
## Dr. Chuck Course
## Author: Grant Gasser

import re, os

def main():
    file = open('regex_sum_242500.txt')

    sum = 0
    for line in file:
        line.rstrip()

        nums = re.findall('[0-9]+', line)

        for num in nums:
            sum += int(num)

    print(sum)


main()
