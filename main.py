epsilon = 10 ** (-10)


def enter_the_matrix_with_file(n, f):
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, f.readline().split())))
    print("Ваша матрица:")
    for i in range(n):
        print(matrix[i])
    print("--------------------")
    return matrix


def enter_the_matrix_with_keyboard(n):
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print("Ваша матрица:")
    for i in range(n):
        print(matrix[i])
    print("--------------------")
    return matrix


def get_first_column(matrix, column):
    n = len(matrix)
    xmax = 0
    line = 0
    for i in range(column, n):
        if xmax < abs(matrix[i][column]):
            xmax = abs(matrix[i][column])
            line = i
    print("Строчка, в которой самый большой элемент в " + str(column + 1) + " столбце - ", line + 1)
    print("--------------------")
    return line


def change_lines(line1, line2, matrix):
    n = len(matrix)
    print("Изначальная матрица:")
    for i in range(n):
        print(matrix[i])
    arr1 = matrix[line1]
    arr2 = matrix[line2]
    matrix[line1] = arr2
    matrix[line2] = arr1
    print("Матрица после изменения строк:")
    for i in range(n):
        print(matrix[i])
    print("--------------------")
    return matrix


def count_scaling_multipliers(matrix, column):
    n = len(matrix)
    multipliers = []
    for i in range(column, n - 1):
        multipliers.append(matrix[i + 1][column] / matrix[column][column])
    print("Масштабирующие множители:")
    print(multipliers)
    print("--------------------")
    return multipliers


def using_multipliers(matrix, multipliers, line, n):
    print("Матрица для изменения:")
    for i in range(n):
        print(matrix[i])
    print("Масштабируемые множители:")
    print(multipliers)
    counter = -1
    for i in range(line + 1, n):
        counter += 1
        for j in range(n + 1):
            matrix[i][j] = -(matrix[line][j] * multipliers[counter] - matrix[i][j])
            if abs(matrix[i][j]) < epsilon:
                matrix[i][j] = 0
    print("Матрица после изменения:")
    for i in range(n):
        print(matrix[i])
    print("--------------------")
    return matrix


def count_determinant(matrix):
    n = len(matrix)
    det = 1
    for i in range(n):
        det *= matrix[i][i]
    print("Определитель матрицы равен - ", round(det))
    return round(det)


def get_solutions(matrix):
    n = len(matrix)
    answers = [0] * n
    for i in range(n - 1, -1, -1):
        ans = matrix[i][-1]
        for j in range(n - 1, i, -1):
            ans = ans - matrix[i][j] * answers[j]
        answers[i] = ans / matrix[i][i]
    print("Корни:")
    for i in range(len(answers)):
        print("x" + str(i + 1) + " = ", answers[i])
    return answers


def get_discrepancy(matrix, solutions):
    n = len(matrix)
    print("Полученная матрица:")
    for i in range(n):
        print(matrix[i])
    print("Полученные корни:")
    print(solutions)
    discrepancies = []
    for i in range(n):
        discrepancy = matrix[i][-1]
        for j in range(n):
            discrepancy -= matrix[i][j]*solutions[j]
        discrepancies.append(discrepancy)
    print("Векторы невязок:")
    print(discrepancies)
    return discrepancies


def solution():
    print("Вы хотите ввести матрицу с клавиатуры или с файла? (к/ф)")
    ans = input()
    if ans == "ф":
        f = open('matrix.txt', 'r')
        n = int(f.readline())
        if n > 20:
            print("Вы ввели значение большее, чем 20")
            print("Не желаете повторить снова? (Да/Нет)")
            answer = input()
            if answer == "Да":
                solution()
            else:
                print("Тогда бывай, браза")
                return 0
        print("--------------------")
        matrix = enter_the_matrix_with_file(n, f)
        for i in range(n - 1):
            biggest = get_first_column(matrix, i)
            change_lines(i, biggest, matrix)
            multipliers = count_scaling_multipliers(matrix, i)
            using_multipliers(matrix, multipliers, i, n)
        print("Итоговая матрица:")
        for i in range(n):
            print(matrix[i])
        print("--------------------")
        count_determinant(matrix)
        print("--------------------")
        solutions = get_solutions(matrix)
        print("--------------------")
        get_discrepancy(matrix, solutions)
        print("--------------------")
    elif ans == "к":
        print("Введите количество строчек в матрице")
        n = int(input())
        if n > 20:
            print("Вы ввели значение большее, чем 20")
            print("Не желаете повторить снова? (Да/Нет)")
            answer = input()
            if answer == "Да":
                solution()
            else:
                print("Тогда бывай, браза")
                return 0
        print("--------------------")
        matrix = enter_the_matrix_with_keyboard(n)
        for i in range(n - 1):
            biggest = get_first_column(matrix, i)
            change_lines(i, biggest, matrix)
            multipliers = count_scaling_multipliers(matrix, i)
            using_multipliers(matrix, multipliers, i, n)
        print("Итоговая матрица:")
        for i in range(n):
            print(matrix[i])
        print("--------------------")
        count_determinant(matrix)
        print("--------------------")
        solutions = get_solutions(matrix)
        print("--------------------")
        get_discrepancy(matrix, solutions)
        print("--------------------")


solution()
