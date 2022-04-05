def out_time(in_sec):
    years = in_sec // num_year
    ostatok_year = in_sec - years * num_year
    days = ostatok_year // num_day
    ostatok_day = ostatok_year - days * num_day
    hours = ostatok_day // num_hour
    ostatok_hour = ostatok_day - hours * num_hour
    minutes = ostatok_hour // num_minute
    seconds = ostatok_hour - minutes * num_minute
    z1=['years', 'days', 'hours', 'minutes', 'seconds']
    z2=[years, days, hours, minutes, seconds]
    slov=dict(zip(z1,z2))
    for i in range(5):

    return slov


num_minute = 60
num_hour = 60 * 60
num_day = 60 * 60 * 24
num_year = 60 * 60 * 24 * 365
print(num_minute)
print(num_hour)
print(num_day)
print(num_year)

x = 1*34 + 60*45 + 3600*15 + 86400*9 + 31536000*6
print(out_time(x))
