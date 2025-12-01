world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
    2022: 'Аргентина'
}

country = 'Италия'

for key, value in world_champions.items():
    print(str(key) + ' - ' + value)


isWin = False
for value in world_champions.values():
    if country in value:
        isWin = True
        break
if not isWin:
    print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке!')
else:
    print(f'{country} cтановилась чемпионом мира по футболу в 21 веке!')