# ведение лога

from datetime import datetime as dt

def write_log(str_item):
    date = dt.now().strftime('%d.%m.%Y')
    time = dt.now().strftime('%H:%M:%S')
    with open('log.csv', 'a', encoding ='utf-8') as file:
        file.write('{};{};{}\n'.format(date, time, str_item))

# def read_log():