lalala = {}
LALALALLALALLAL = "wewewewewew"
times = '1h 45m,360s,25m,30m 120s,2h 60s'
replaced_symbols = [' ']

for s in replaced_symbols:
    times = times.replace(s, ',').split(',')
    print(times)
    for w in times:
        if "1h" == w:
            w = w.replace('h', '')
            a = int(w) * 60
        elif "2h" == w:
            w = w.replace('h', '')
            b = int(w) * 60
        elif '45m' == w:
            w = w.replace('m', '')
            c = int(w)
        elif '25m' == w:
            w = w.replace('m', '')
            d = int(w)
        elif '30m' == w:
            w = w.replace('m', '')
            e = int(w)
        elif '360s' == w:
            w = w.replace('s', '')
            f = int(w) // 60
        elif '120s' == w:
            w = w.replace('s', '')
            g = int(w) // 60
        elif '60s' == w:
            w = w.replace('s', '')
            h = int(w) // 60
    print(a + b + c + d + e + f + g + h)




