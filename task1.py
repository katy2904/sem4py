# Задайте натуральное число N. Напишите программу, которая составит список простых
# множителей числа N.

n = int(input('Ввведите число: '))
lst = [2]
for i in range(3, n):
    if (i % 2 == 0) or (i % 10 == 0) or (i != 5 and i % 5 == 0):
        continue
    else:
        lst.append(i)

for i in lst:
    if i ** 2 in lst:
        lst.remove(i ** 2)

    for j in lst:
        if j % i == 0 and j != i:
            lst.remove(j)

print(lst)