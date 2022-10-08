# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

lst = [1, 8, 22, 5, 4, 7, 6, 21, 852, 56, 26, 4, 2, 5, 7, 2, 3, 6, 8, 5, 4]
final_list = []
for i in lst:
    if lst.count(i) == 1:
        final_list.append(i)

print(final_list)


#без использования метода .count решение было бы таким:

count = 0
for i in lst:
    for j in lst:
        if i == j:
            count += 1
    if count == 1:
        final_list.append(i)
    count = 0
print(final_list)