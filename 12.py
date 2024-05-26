def get_matrix (n, m, value):
    for i in range(n):
        mot = []
        mat.append(mot)
        for j in range(m):
            mot.append(value)
    return mat

mat = []
n = int(input("Введите число строк: "))
m = int(input("Введите число столбцов: "))
k = int(input("Введите число заполнения: "))
print(get_matrix(n, m, k))