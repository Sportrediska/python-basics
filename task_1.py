string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_in_minutes = []
string = string.replace(',', ' ').split()

for s in string:
    if 'h' in s:
        s = int(s[:-1]) * 60
        time_in_minutes.append(s)
    elif 'm' in s:
        s = int(s[:-1])
        time_in_minutes.append(s)
    else:
        s = int(s[:-1]) // 60
        time_in_minutes.append(s)

        
print('Всего', sum(time_in_minutes), 'минут')