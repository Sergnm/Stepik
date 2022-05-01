#           Пропущенные комменты
with open(r'C:\Users\sergnm\Downloads\cyrillic1.txt', 'r', encoding='utf-8') as file:
    sp = list(map(str.strip, file.readlines()))
    test = []
    # print(sp)
    # print(len(sp))
    for i in range(len(sp)):
        if sp[i].startswith('def ') and not sp[i - 1].startswith('#'):
            test.append(sp[i][4:sp[i].find('(')])
    if len(test) == 0:
        print("Best Programming Team")
    else:
        print(*test, sep='\n')
