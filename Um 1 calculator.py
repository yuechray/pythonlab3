def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Ошибка: Деление на ноль невозможно.")
    return a / b

def power(a: float, b: float) -> float:
    return a ** b

def input_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def main():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power
    }

    while True:
        print("\nДоступные операции: +, -, *, /, **, exit")
        operation = input("Выберите операцию: ").strip()

        if operation == 'exit':
            print("Выход из программы.")
            break

        if operation in operations:
            a = input_number("Введите первое число: ")
            b = input_number("Введите второе число: ")

            try:
                result = operations[operation](a, b)
                print(f"Результат: {a} {operation} {b} = {result}")
            except ZeroDivisionError as e:
                print(e)
        else:
            print("Ошибка: операция не поддерживается.")

if __name__ == "__main__":
    main()