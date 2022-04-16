
sum = 0

tickets = int(input('Введите, сколько билетов хотите приобрести? '))
for i in range(tickets):
    age = int(input(f'Сколько лет {i + 1} -му посетителю? '))
    if age < 18:
        sum = sum + 0
    elif 18 <= age < 25:
        sum = sum + 990
    else:
        sum = sum + 1390
if tickets > 3:
    sum = int(sum - sum / 100 * 10)
    print(f'К оплате с учетом скидки {sum} рублей')
else:
    print(f'К оплате {sum} рублей')