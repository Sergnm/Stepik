#           Статистика по файлу
import string
from functools import reduce
from operator import *

with open(r'C:\Users\sergnm\Downloads\file.txt', 'r', encoding='utf-8') as file:
    tot1, tot2, tot3 = 0, 0, 0
    for line in file:
        tot1 += 1
        sp = line.strip().split()
        tot2+=len(sp)
        for i in range(len(sp)):
            for j in range(len(sp[i])):
                if sp[i][j] in string.ascii_letters:
                    tot3+=1
    print(f'Input file contains:\n{tot3} letters\n{tot2} words\n{tot1} lines')