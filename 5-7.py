#Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

my_json = open('text_json.json', 'w', encoding='utf-8')
my_file = open('text_7.txt', encoding='utf-8')
mydict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_file}
list = [mydict, {'average profit': round(sum([int(i) for i in mydict.values() if int(i) > 0]) /
                                       len([int(i) for i in mydict.values() if int(i) > 0]))},
        {'average loss': round(sum([int(i) for i in mydict.values() if int(i) <= 0]) /
                               len([int(i) for i in mydict.values() if int(i) <= 0]))}]
json.dump(list, my_json, ensure_ascii=False, indent=4)
my_file.close()
my_json.close()
