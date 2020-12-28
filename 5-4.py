#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

file = open('text_4.txt', 'r', encoding='utf-8')
new_file = open('text_4_new.txt', 'w', encoding='utf-8')
dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
for i in file:
    string = i.split()
    for key in dict:
        if string[0] == key:
            string[0] = dict.get(key)
            new_file.write(str(' '.join(string)) + '\n')
new_file.close()
file.close()
