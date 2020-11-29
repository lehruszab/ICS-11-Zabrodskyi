def get_dovidnik():
    with open("./data/dovidnik.txt", encoding='utf-8') as dovidnik_file: # encoding='utf-8' - нужно чтобы коректно отображать руские буквы, а не символы непонятные
        from_dovidnik = dovidnik_file.readlines()

    dovidnik_list = [] 

    for line in from_dovidnik:
        line_list = line.split(';')
        dovidnik_list.append(line_list)
      
      
    return dovidnik_list

def get_tovaroobig():
    with open("./data/tovaroobig.txt", encoding='utf-8') as tovaroobig_file:
        from_tovaroobig = tovaroobig_file.readlines()

    tovaroobig_list = [] 

    for line in from_tovaroobig:
        line_list = line.split(';')
        tovaroobig_list.append(line_list)
      
    return tovaroobig_list

def show_dovidnik(dovidnik):
    dovidnik_code_from = input("З якого коду товарної групи?")
    dovidnik_code_to = input("По який код товарної групи?")

    kol_lines = 0

    for cod in dovidnik:
        if dovidnik_code_from <= cod[0] <= dovidnik_code_to:
            print("Код: {:8} Назва:{:20} Торгова скидка:{:4}".format(cod[0], cod[1], cod[2].rstrip()))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(dovidnik_code_from, dovidnik_code_to))

def show_tovaroobig(tovaroobig):
    tovaroobig_code_from = input("З якого коду товарної групи?")
    tovaroobig_code_to = input("По який код товарної групи?")

    kol_lines = 0

    for cod in tovaroobig:
        if tovaroobig_code_from <= cod[0] <= tovaroobig_code_to:
            print("Код:{:7} План:{:8} Очікуємо виконання:{:8} Рік:{:6}".format(cod[0], cod[1], cod[2], cod[3].rstrip()))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(tovaroobig_code_from, tovaroobig_code_to))



# what_show = int(input("Показати: 1 - довідник; 2 - товарообіг? (1/2)"))
# if what_show == 1:
#dovidnik = get_dovidnik()
#show_dovidnik(dovidnik)   
# elif what_show == 2:
#tovaroobig = get_tovaroobig()
#show_tovaroobig(tovaroobig)
# else:
#    print("Введіть '1' або '2'!")  
