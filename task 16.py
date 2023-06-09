# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в списке A. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны
# N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5 
# 1 2 3 4 5
# 3
# -> 1

print("\033[43m\0")
N = abs(int(input('Введите количество элементов списка А: ')))
print("\033[42m\0")
A_line = input("Введите элементы списка: ")
A_num = list(map(int, A_line))
if len(A_num) != N:
    print("\033[41m\0")
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    print("\033[45m\0")
    X = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
            print("\033[46m\0")
    print(f'Число {X} встречается в списке A {count} раз') 
    