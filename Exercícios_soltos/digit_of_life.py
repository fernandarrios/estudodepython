year = '20000101'

while len(year) != 1:
    sum_of_digits = 0
    for digit in year:
        sum_of_digits += int(digit)
    year = str(sum_of_digits)
print(sum_of_digits)