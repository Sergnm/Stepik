with open(r'C:\Users\sergnm\Downloads\logfile.txt', 'r', encoding='utf-8') as input_file, open(
        r'C:\Users\sergnm\Downloads\output.txt', 'w', encoding='utf-8') as output_file:
    for line in input_file:
        sp = line.strip().split()
        if (int(sp[3][:2])*60+int(sp[3][3:]))-(int(sp[2][:2])*60+int(sp[3][3:]))>=60:
            print(*sp, file=output_file)