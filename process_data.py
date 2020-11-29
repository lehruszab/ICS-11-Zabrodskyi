from data_service import get_dovidnik, get_tovaroobig

dohod = {
    'name'                  : "",       # найменування товарної групи
    'year'                  : 0,        # рік
    'plan_tovaroobig'       : 0,      # план товарообігу в грн
    'ochikuvane_tovaroobig' : 0,      # очікуване виконання товарообігу в грн
    'discount'              : 0,      # токргова скидка в %
    'plan_dohod'            : 0,      # план валового доходу в грн
    'ochikuvane_dohod'      : 0       # очікуване виконання доходу в грн
}



def create_dohod():
    dovidniks = get_dovidnik()
    tovaroobigs = get_tovaroobig()

    def get_dovidnik_name(dovidnik_code):
        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[1]
        return "*** назва не знайдена"

    def get_dovidnik_discount(dovidnik_code):
        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[2]
        return "*** назва не знайдена"
    dohod_list = []
    


    for tovaroobig in tovaroobigs:
        dohod_copy = dohod.copy()  

        dohod_copy['name']                  = get_dovidnik_name(tovaroobig[0])
        dohod_copy['year']                  = tovaroobig[3].rstrip()
        dohod_copy['plan_tovaroobig']       = tovaroobig[1]
        dohod_copy['ochikuvane_tovaroobig'] = tovaroobig[2]
        dohod_copy['discount']              = float(get_dovidnik_discount(tovaroobig[0]))
        dohod_copy['plan_dohod']            = int(dohod_copy['plan_tovaroobig']) * int(dohod_copy['discount'] * 10) / 10
        dohod_copy['ochikuvane_dohod']      = int(dohod_copy['ochikuvane_tovaroobig']) * int(dohod_copy['discount'] * 10) / 10
        dohod_list.append(dohod_copy)
    return dohod_list
#result = create_dohod()

#for line in  result:
#    print(line)