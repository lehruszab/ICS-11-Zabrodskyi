def get_dovidnik():
    

    with open("./data/dovidnik.txt") as dovidnik_file:
        from_dovidnik = dovidnik_file.readlines()

    
    dovidnik_list = [] 

    for line in from_dovidnik:
        line_list = line.split(';')
        dovidnik_list.append(line_list)
      
    return dovidnik_list




def show_dovidnik(dovidnik):
    dovidnik_code_from = input("З якого коду клієнта?")
    dovidnik_code_to = input("По який код клієнта?")

    kol_lines = 0

    for c in dovidnik:
        if dovidnik_code_from <= c[0] <= dovidnik_code_to:
            print("Код: {:6} Назва: {:16} Торгова скидка: {:20}".format(c[0], c[1], c[2]))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом {} не знайдено".format(dovidnik_code_from))

dovidnik = get_dovidnik()
show_dovidnik(dovidnik)   
