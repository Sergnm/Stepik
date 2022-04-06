def out_time(in_sec):
    years = in_sec // num_year
    ostatok_year = in_sec - years * num_year
    days = ostatok_year // num_day
    ostatok_day = ostatok_year - days * num_day
    hours = ostatok_day // num_hour
    ostatok_hour = ostatok_day - hours * num_hour
    minutes = ostatok_hour // num_minute
    seconds = ostatok_hour - minutes * num_minute
    slov = {1: [years, 'years'],
            2: [days, 'days'],
            3: [hours, 'hours'],
            4: [minutes, 'minutes'],
            5: [seconds, 'seconds']}
    text = ''
    for key, value in slov.items():
        if value[0] == 0:
            continue
        text += str(value[0]) + ' ' + value[1] + ', '
    text = text[:-2]
    return text


num_minute = 60
num_hour = 60 * 60
num_day = 60 * 60 * 24
num_year = 60 * 60 * 24 * 365
# print(num_minute)
# print(num_hour)
# print(num_day)
# print(num_year)

x = 1 * 34 + 60 * 45 + 3600 * 12 + 86400 * 9 + 31536000 * 6
print(out_time(x))
