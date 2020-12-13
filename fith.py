#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
#результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
#(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль
#фирмы в расчете на одного сотрудника.

proceeds = int(input('Enter proceeds value: '))
costs = int(input('Enter costs value: '))
if proceeds > costs:
    print('The company worked profitably. Profitability: %.2f' % (proceeds / costs))
    headcount = int(input('Enter headcount in company: '))
    print('Profit per employee: %.2f' % ((proceeds - costs)/headcount))
elif costs > proceeds:
        print('The company worked with loss.')
else:
    print('The company worked with zero profit')
