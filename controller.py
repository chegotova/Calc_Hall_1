#связующее звено между модулями

import complex_sum as c_sum
import complex_sub as c_sub
import logger as log
import util
#import rational as rat
import view

def hello():
    '''
    Вызов приветствия и вызов функции выбора типа вычислений
    '''
    view.say_hello()
    action()


def action():
    '''
    Выбор типа вычислений и вызов соответствующей функции
    '''
    mode = view.select_mode()
    match mode:
        case '1':
            print('Пока заглушка')
        case '2':
            print('Пока заглушка')
        case '3':
            print('Пока заглушка')
        case '4':
            print('Пока заглушка')
        case '5':
            button_click(5)
        case '6':
            button_click(6)    


def button_click(mode: int):
    '''
    Ввод данных для вычисления комплексных чисел и вычисление
    '''
    value_a = view.get_complex_value('a', 'действительное')
    value_b = view.get_complex_value('a', 'мнимое')
    value_c = view.get_complex_value('b', 'действительное')
    value_d = view.get_complex_value('b', 'мнимое')
    x = complex(value_a, value_b)
    y = complex(value_c, value_d)
    if mode == 5:
        c_sum.init(x, y)
        result = c_sum.do_it()
        view.view_data(result, 'sum')
        log.write_log(util.mode_decoder(str(mode)))
    elif mode == 6:
        c_sub.init(x, y)
        result = c_sub.do_it()
        view.view_data(result, 'sub')
        log.write_log(util.mode_decoder(str(mode)))