def sum_digits(number):
    sp = list(str(number))
    if sp[0] == '-':
        sp = sp[1:]
    return sum(list(map(int,sp)))

num = -205
print(sum_digits(num))
