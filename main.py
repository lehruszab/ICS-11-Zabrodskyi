import os
from process_data import create_dohod
from data_service import show_dovidnik, show_tovaroobig, get_tovaroobig, get_dovidnik  
import codecs

MAIN_MENU = \
"""
~~~~~~~~~~~~~~~~~~~~~ ОБРОБКА ВАЛОВОГО ДОХОДУ УНІВЕРМАГУ НА ПОТОЧНИЙ РІК ~~~~~~~~~~~~~~~~~~~~~ 

1 - вивід доходу на екран
2 - запис доходу в файл
3 - вивід товарообігу універмагу
4 - вивід довідника товарних груп
0 - завершити роботу
_________________________________
"""

TITLE = "ВАЛОВИЙ ДОХОД УНІВЕРМАГУ НА ПОТОЧНИЙ РІК"
HEADER = \
'''
=======================================================================================================
|  Найменування  |  Рік  |      Товарообіг, тис.грн.     |  Торгова  |    Валовий доход, тис.грн.     |
| товарної групи |       |===============================| скидка, % |================================|
|                |       |   План   | Очікуване виконная |           |   План   | Очікуване виконання | 
=======================================================================================================
'''
FOOTER = \
'''
=====================================================================================================
'''

STOP_MESSAGE = "Нажміть будь-яку клавішу для продовження"


def show_dohod(dohod_list):
    print(f'\n\n{TITLE:^103}')
    print(HEADER)
    
    for dohod in dohod_list:
        print(f"{dohod['name']:17}", 
              f"{dohod['year']:^7}",
              f"{dohod['plan_tovaroobig']:^10}",
              f"{dohod['ochikuvane_tovaroobig']:^20}",
              f"{dohod['discount']:^11.1f}",
              f"{dohod['plan_dohod']:^12.1f}",
              f"{dohod['ochikuvane_dohod']:^20.1f}"
              )
    print(FOOTER)  
    
def write_file(dohod_list):
    with codecs.open('./data/dohod.txt', "w",  encoding='utf-8') as dohod_file:
        for dohod in dohod_list:
            line = \
                f"{(dohod['name']) + ';':20}"                   + \
                f"{(dohod['year']) + ';':8}"                    + \
                f"{(dohod['plan_tovaroobig']) + ';':8}"         + \
                f"{(dohod['ochikuvane_tovaroobig']) + ';':8}"   + \
                f"{(str(dohod['discount'])) + ';':7}"           + \
                f"{(str(dohod['plan_dohod'])) + ';':11}"        + \
                f"{(str(dohod['ochikuvane_dohod'])) + ';':9}" + '\n'
            
            dohod_file.write(line)
    
    print("Файл успішно сформовано ...")
            


while True: 
    os.system('clear')
    print(MAIN_MENU)
    command_number = input('Введіть номер команди: ')
    
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)

    elif command_number == '1':
        dohod_list = create_dohod()
        show_dohod(dohod_list)  
        input(STOP_MESSAGE)  

    elif command_number == '2':
        dohod_list = create_dohod()
        write_file(dohod_list)
        input(STOP_MESSAGE)

    elif command_number == '3':
        tovaroobigs = get_tovaroobig()
        show_tovaroobig(tovaroobigs)
        input(STOP_MESSAGE)

    elif command_number == '4':
        dovidniks = get_dovidnik()
        show_dovidnik(dovidniks)
        input(STOP_MESSAGE)