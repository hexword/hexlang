def PreparationCode(code: list[str]) -> list[str]:
    new_code = [] # тут будут обновленные строки кода
    for line in code:

        # убрать перенос строки, и пробелы в начале строки
        line = line.replace("\n", "").lstrip()

        # добавление строки кода
        if line != "":
            new_code.append(line)
        else:
            new_code.append("# 0")

    return new_code