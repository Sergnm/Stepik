def out_time(in_sec):
    minuta = 60
    chas = 60 * 60
    den = 60 * 60 * 24
    god = 60 * 60 * 24 * 365

    gody = in_sec // god
    ostatok_god = in_sec % god

    dni = ostatok_god // den
    ostatok_den = ostatok_god % den

    return (ggod, ggod_ostatok)


in_seconds = int(input())
print(out_time(in_seconds))
