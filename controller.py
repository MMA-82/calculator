import ui
import oper


def start():
    #example = view.get_examp()
    correct_example = oper.concat_examp(ui.get_examp())

    origin_example = oper.copy_examp(correct_example)

    
    while len(correct_example) > 1:
        result = oper.calculate('/', '*', correct_example)
        result = oper.calculate('+', '-', correct_example)
        

    ui.print_result(origin_example, result)

