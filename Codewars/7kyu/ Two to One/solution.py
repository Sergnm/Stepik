def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


s1 = str('xyaabbbccccdefww')
s2 = str('xxxxyyyyabklmopq')
print(longest(s1, s2))
