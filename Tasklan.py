from pywebio.input import input, TEXT
from pywebio.output import *


s1 = put_text('Задачи высокого приоритета')
s2 = put_text('Задачи средниго приоритета')
s3 = put_text('Задачи низкого приоритета')
def main():
    
    style(s1, 'color:red')
    style(s2, 'color:Orange')
    style(s3, 'color:green')

    put_table([
        [s1, s2, s3],
        [input('ведите задачу высокого приоритета'), input('ведите задачу среднего приоритета'), input('ведите задачу низкого приоритета')],
        [input('ведите задачу высокого приоритета'), input('ведите задачу среднего приоритета'), input('ведите задачу низкого приоритета')],])

if __name__ == '__main__':
    main()