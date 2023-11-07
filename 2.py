n, m = map(int, input("Укажите размеры n и m : ").split())
array = []
for k in range(n):
    row = list(map(int, input("Укажите строку : ").split()))
    array.append(row)
i, j = map(int, input("Укажите столбцы i и j: ").split())
for row in array:
    row[i], row[j] = row[j], row[i]
for row in array:
    print(*row)