

def concat_examp(example):
    example = example.replace(' ', '').replace('+', ' + ').\
    replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    if example.startswith(' - '):
        example = '-' + example[3:]
    return example.split()

def copy_examp(correct_example):
    return correct_example.copy()

def calculate(oper_1, oper_2, example):
    operation = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,}
    i = 0
    while oper_1 in example or oper_2 in example:
        if example[i] in [oper_1, oper_2]:
            example[i-1] = operation.get(example[i])(int(example[i -1]), int(example[i + 1]))
            example.pop(i)
            example.pop(i)
        else:
            i += 1
    return example
                








