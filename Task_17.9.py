

L = '1 4 6 32 2 98 7 65 12 61 91 8 13 17 73 4 54 12'
l_list = list(map(int, L.split()))

def sort_f(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array

sort_list = sort_f(l_list)
print("Отсортированный список:", sort_list)

len_list = len(sort_list)

num = int(input('Введите целое число: '))
while sort_list[0] > num or num > sort_list[-1]:
    print('Число не удовлетворяет условию. Введите другое число')
    num = int(input('Введите целое число: '))

def binary_search(array, element, left, right):
    if left > right:
        return 'введенный элемент отсутствует в списке'

    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print('Позиция искомого элемента: ', binary_search(sort_list, num, 0, len_list))