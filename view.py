#user interface
import util

def view_data(data, title: str):
    '''
    Вывод результата вычисления
    '''
    print(f'{title} = {data}')


def get_complex_value(a: str, r: str):
    '''
    Ввод значения для вычисления комплексных чисел с проверкой введенных данных.
    TODO: подумать на предмет универсальности
    '''
    while True:
        data = input('{} значение {}= '.format (r, a))
        if not util.is_number(data):
            print('Это не число, повторите ввод.')
        else:
            return int(data)
    


def say_hello():
    '''
    Просто приветствие
    '''
    print('Привет! Можем посчитать: ')
    print('''   
    1. Сложение рациональных чисел
    2. Вычитание рациональных чисел
    3. Умножение рациональных чисел
    4. Деление рациональных чисел
    5. Сложение комплексных чисел
    6. Вычитание комплексных чисел
            ''')
  

def select_mode():
    '''
    Ввод выбора типа вычисления с проверкой введенных данных
    '''
    while True:
        mode = input('Выберите тип вычисления из списка: ')
        if not mode.isdigit() or int(mode) < 1 or int(mode) > 6:
            print('Выбран неверный тип, повторите ввод.')
        else:
            return mode


