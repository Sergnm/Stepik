import random
from functools import reduce
#file = open(r'D:\TEMP_Virtual\lines.txt', 'r', encoding='utf-8')

'''for line in file:
    print(line.strip())
'''
#           Метод read()
'''content = file.read()
file.close()
print('<<<<<<<<<<=========================>>>>>>>>>>>>')
print(content)
print('<<<<<<<<<<=========================>>>>>>>>>>>>')
'''
#           Метод readline()
'''
print('<<<<<<<<<<=========================>>>>>>>>>>>>')
for line in file:
    print(line.strip())
file.close()'''
#           Метод readlines()
"""print('<<<<<<<<<<=========================>>>>>>>>>>>>')
languages = list(map(str.strip, file.readlines()))
file.close()
print(random.choice(languages))"""
#           Сумма двух-1
"""
file = open(r'D:\TEMP_Virtual\numbers.txt', 'r', encoding='utf-8')
tot=0
for line in file:
    tot+=int(line.strip())
file.close()
print(tot)"""
#           Сумма двух-2
'''
file = open(r'D:\TEMP_Virtual\nums.txt', 'r', encoding='utf-8')
tot = 0
for line in file:
    if len(line.strip()) != 0:
        tot += int(line.strip())
file.close()
print(tot)'''
#           Общая стоимость
'''file = open(r'D:\TEMP_Virtual\prices.txt', 'r', encoding='utf-8')
tot = 0
for line in file:
    x=line.strip().split('\t')
    tot+=int(x[2])
file.close()
print(tot)
'''
