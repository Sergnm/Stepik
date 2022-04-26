#           Длинные строки
with open(r'C:\Users\sergnm\Downloads\lines.txt', 'r', encoding='utf-8') as file:
    languages = list(map(str.strip, file.readlines()))
    maxx = max([len(languages[i]) for i in range(len(languages))])
    sp=[print(i) for i in languages if len(i)==maxx]
