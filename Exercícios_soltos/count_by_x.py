def count_by(x, count) :
    numbers_in_range = []
    for i in range(x, (count*x + 1), x):
        numbers_in_range.append(i)
    return numbers_in_range


x = 2
count = 5
for i in range(x, count*x +1, x):
    print(i)
