def calculator():
    print("Калькулятор поддерживает следующие операции:")
    print("Арифметические: +, -, *, /, //, %, **")
    print("Сравнение: ==, !=, >, <, >=, <=")
    print("Логические: and, or, not")
    print("Побитовые: &, |, ^, ~, <<, >>")
    print("Принадлежность: in, not in")
    print("Тождественность: is, is not")

    try:

        a = input("Введите первое значение: ")
        if a.isdigit():
            a = int(a)
        elif a.replace('.', '', 1).isdigit():
            a = float(a)

        operator = input("Введите оператор: ")


        b = input("Введите второе значение: ")
        if b.isdigit():
            b = int(b)
        elif b.replace('.', '', 1).isdigit():
            b = float(b)


        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                raise ValueError("Деление на ноль!")
            result = a / b
        elif operator == '//':
            if b == 0:
                raise ValueError("Деление на ноль!")
            result = a // b
        elif operator == '%':
            if b == 0:
                raise ValueError("Деление на ноль!")
            result = a % b
        elif operator == '**':
            result = a ** b
        elif operator == '==':
            result = a == b
        elif operator == '!=':
            result = a != b
        elif operator == '>':
            result = a > b
        elif operator == '<':
            result = a < b
        elif operator == '>=':
            result = a >= b
        elif operator == '<=':
            result = a <= b
        elif operator == 'and':
            result = bool(a) and bool(b)
        elif operator == 'or':
            result = bool(a) or bool(b)
        elif operator == 'not':
            result = not bool(b)
        elif operator == '&':
            result = a & b
        elif operator == '|':
            result = a | b
        elif operator == '^':
            result = a ^ b
        elif operator == '~':
            result = ~a
        elif operator == '<<':
            result = a << b
        elif operator == '>>':
            result = a >> b
        elif operator == 'in':
            result = str(a) in str(b)
        elif operator == 'not in':
            result = str(a) not in str(b)
        elif operator == 'is':
            result = a is b
        elif operator == 'is not':
            result = a is not b
        else:
            raise ValueError("Неизвестный оператор!")

        print(f"Результат: {result}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")


calculator()