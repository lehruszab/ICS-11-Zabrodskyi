from data_service import get_dovidnik, get_tovaroobig

dohod = {
    'name'                  : "",       # найменування товарної групи
    'year'                  : 0,        # рік
    'plan_tovaroobig'       : 0.0,      # план товарообігу в грн
    'ochikuvane_tovaroobig' : 0.0,      # очікуване виконання товарообігу в грн
    'discount'              : 0.0,      # токргова скидка в %
    'plan_dohod'            : 0.0,      # план валового доходу в грн
    'ochikuvane_dohod'      : 0.0       # очікуване виконання товарообігу в грн
}

orders = get_dovidnik
print(orders)