#           *********
sp=[str(i) for i in range(int(input()))]
for i in range(len(sp)):
    with open(sp[i], 'r', encoding='utf-8') as input_file, open(
        'answer.txt', 'a', encoding='utf-8') as output_file:
        print(input_file.read(), file=output_file)

#           Goooood students
from operator import *
from functools import reduce
def fff(x):
    return all([int(i)>=65 for i in x.split()[1:]])

with open(r'C:\Users\sergnm\Downloads\grades1.txt', 'r', encoding='utf-8') as input_file:
    sp = list(map(fff,list(map(str.strip, input_file.readlines())))).count(True)
    print(sp)

#           Самое длинное слово в файле

with open(r'C:\Users\sergnm\Downloads\words2.txt', 'r', encoding='utf-8') as input_file:
    sp = list(map(str.strip, input_file.readlines()))
    if len(sp)<10:
        print(*sp,sep='\n')
    else:
        print(*sp[-10:],sep='\n')

with open(r'C:\Users\sergnm\Downloads\cyrillic.txt', 'r', encoding='utf-8') as input_file, open(
        r'C:\Users\sergnm\Downloads\transliteration.txt', 'w', encoding='utf-8') as output_file:
    d = {
        'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
        'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
        'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
        'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
        'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'CH',
        'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
        'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
        'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya'
    }
    sp = input_file.read()
    print(sp, '', sep="\n")
    for key, value in d.items():
        if key in sp:
            sp = sp.replace(key, value)
    print(sp, file=output_file)


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
