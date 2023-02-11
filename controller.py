import ui
import operator


def start():
    #example = view.get_examp()
    correct_example = operator.concat_examp(ui.get_examp())

    origin_example = operator.copy_examp(correct_example)

    
    while len(correct_example) > 1:
        result = operator.calculate('/', '*', correct_example)
        result = operator.calculate('+', '-', correct_example)
        

    ui.print_result(origin_example, result)

