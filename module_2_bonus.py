def generate_password():
    # Итерация по всем числам от 3 до 20
    for n in range(3, 21):
        password = ""  # Переменная для хранения результата
        # Итерация по всем возможным парам
        for i in range(1, 21):
            for j in range(i + 1, 21):  # Учитываем только пары, где i < j
                if n % (i + j) == 0:  # Проверяем кратность
                    password += str(i) + str(j)  # Формируем строку результата

        print(f"{n} - {password}")


# Запуск функции
generate_password()
