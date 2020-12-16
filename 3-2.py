# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data(Name='Noname', Surname='Nosurname', birth_year=2000, city='Nocity', email='Noemail', phone='Nophone'):
    print(f'Name: {Name} | Surname: {Surname} | birth_year: {((birth_year+1900) if birth_year < 100 else birth_year):04} | City: {city} | Email: {email} | Phone: {phone}')

user_data('Leonid', 'Bukreev', city='SPB', birth_year=86, email='lordestik@mail.ru')
b = 100
print(f'{(b+1900) if b < 100 else b }')