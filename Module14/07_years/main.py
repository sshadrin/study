def years(year, yaear_1):
    for i in range(year, yaear_1 + 1):
        a = i // 1000
        b = i // 100 % 10
        c = i // 10 % 10
        d = i % 10
        if a == b == c or a == b == d or a == c == d or b == c == d:
            print(i)


year = int(input('Введите первый год:'))
year_1 = int(input('Введите второй год:'))
print(f'Года от {year} до {year_1} с тремя одинаковыми цифрами:')
years(year, year_1)
