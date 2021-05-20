# from requests import get, utils
# keys_of_currency_list = {
#     # 'valute_ID' : 'Valute ID',
#     'num_code' : 'NumCode',
#     'CharCode' : 'CharCode',
#     'nominal_valute' : 'Nominal',
#     'name_valute' : 'Name'
#     }
# # keys = 'Valute ID' 'NumCode' 'CharCode' 'Nominal Name'
#
# def get_currency_list():
#     response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
#     content = response.replace('</' or '>', ' ')
#     content = content.split('><')
#     return content
#
# print(get_currency_list())
#
# currency_dict = {}
# for item in get_currency_list():
#     for key in keys_of_currency_list.values():
#         if not item.find(key) ==-1:
#             value_of_currency_list = item[len(key)+1:-len(key)]
#             print(key,value_of_currency_list)
#             currency_dict.setdefault(key[value_of_currency_list])
# # print(currency_dict)
#
# Александр, привет. Выше мой *овнокод, в котором я пытался победить строку с курсами валют. Как я не пытался сделать по своему, но у меня не вышло.
# Я убил кучу времени, скурил пол гугла по работе со строками и словарями, но так и не победил его. Была задумка сделать словарь с ключем по Valute ID. И потом с ним работать.
# Может быть окинешь своим опытным взором на этот код, и скажешь что я был на правильном пути. Или же это было изначально плохой идеей
#
# К сожалению, как и у большинства взрослых людей, времени очень мало. Существует еще куча вещей которым тоже нужно уделять внимание.
# Поэтому снова извиняюсь за копипасту твоего решения. Но скажу, что я его прогонял через дебаггер и разобрался как оно работает.
# Ну и плюс переписывание кода вручную тоже способствует пониманию
#

from datetime import date
from decimal import Decimal
import requests


def get_currency_rate(currency_code='USD'):
    currency_code = currency_code.upper()
    response_text = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_starts_at_index = response_text.find(currency_code)
    if currency_starts_at_index == -1:
        return

    date_index = response_text.find('Date')

    currency_date = response_text[date_index + 6:date_index + 16]
    day, month, year = (int(x) for x in currency_date.split('.'))
    refined_currency_date = date(year,month,day)

    nominal = getField('<Nominal>', response_text, currency_starts_at_index)
    currency_price = \
        getField('<Value>', response_text, currency_starts_at_index)
    currency_price = currency_price.replace(',','.')
    return f'На {refined_currency_date} {nominal} {currency_code} == ' \
            f'{Decimal(currency_price)} RUR'

def getField(field_name, response_text,currency_start_at_index):
    value_start_index = response_text.find(field_name,currency_start_at_index) + len(field_name)
    value_end_index = response_text.find('</',value_start_index)
    return response_text[value_start_index:value_end_index]

if __name__ == '__main__':
    from sys import argv
    _module_name, currency_code_arg = argv
    print(get_currency_rate(currency_code_arg))