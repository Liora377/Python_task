#вариант 1

money = float(input('Введите сумму вклада: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = []
for i in per_cent:
    deposit.append(int(money /100 * per_cent[i]))

deposit_max = max(deposit)

print('Варианты накоплений: ', deposit)
print('Максимальная сумма, которую вы можете заработать - ', (deposit_max))

#вариант 2

money = float(input('Введите сумму вклада: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_list = list(per_cent.values())
deposit = []
deposit.append(int(money / 100 * per_cent_list[0]))
deposit.append(int(money / 100 * per_cent_list[1]))
deposit.append(int(money / 100 * per_cent_list[2]))
deposit.append(int(money / 100 * per_cent_list[3]))

deposit_max = max(deposit)

print('Варианты накоплений: ', deposit)
print('Максимальная сумма, которую вы можете заработать - ', (deposit_max))
