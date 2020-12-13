#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
sec = int(input("Enter amount of seconds: "))
hh = sec // 3600
mm = (sec // 60) % 60
ss = sec % 60

if hh < 10:
    hh = '0' + str(hh)
else:
    hh = str(hh)
if mm < 10:
    mm = '0' + str(mm)
else:
    mm = str(mm)
if ss < 10:
    ss = '0' + str(ss)
else:
    ss = str(ss)
print(f"{hh}:{mm}:{ss} !")