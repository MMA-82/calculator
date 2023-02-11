def get_examp():
    example = input('Введите выражение, используя знаки +, -, *, /: ')
    return example

def print_result(origin, result):
    print('Результат выражения:')
    print(f'{" ".join(origin)} = {round(result[0], 2)}')