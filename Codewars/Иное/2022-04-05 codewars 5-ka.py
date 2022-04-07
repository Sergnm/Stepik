def out_time(in_sec):
    num_minute, num_hour = 60, 3600  # переменные
    hours = in_sec // num_hour
    minutes = (in_sec % num_hour) // num_minute
    seconds = (in_sec % num_hour) % num_minute
    if hours < 10:
        h = '0' + str(hours)
    else:
        h = str(hours)
    if minutes < 10:
        m = '0' + str(minutes)
    else:
        m = str(minutes)
    if seconds < 10:
        s = '0' + str(seconds)
    else:
        s = str(seconds)
    return h + ':' + m + ':' + s


x = 59 * 1 + 59 * 60 + 99 * 3600
print(out_time(x))
