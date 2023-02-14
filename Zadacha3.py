def time_sort():
    time_count = int(input("сколько временных циклов вы хотите ввести - "))
    c = 0
    data = []
    while c < time_count:
        c += 1
        time = input('введите время - ')
        if len(time) < 8:
            print("вводите правильно пример:\n"
                  "09:45:35")
            continue
        else:
            data.append(time)
            print(sorted(data)[::-1])


time_sort()