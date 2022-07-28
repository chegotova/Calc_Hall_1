def is_number(str): #проверка, являются ли введенные данные числом
    try:
        int(str)
        return True
    except ValueError:
        return False

def mode_decoder(mode: str):
    '''
    Дешифровка типов вычислений для лог файла
    '''
    s = ''
    match mode:
        case '1':
            s = 'Сложение рациональных чисел'       
        case '2':
            s = 'Вычитание рациональных чисел'
        case '3':
            s = 'Умножение рациональных чисел'          
        case '4':
            s = 'Деление рациональных чисел'
        case '5':
            s = 'Сложение комплексных чисел'            
        case '6':
            s = 'Вычитание комплексных чисел'
    return s

      