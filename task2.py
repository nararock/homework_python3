def get_info(name, surname, year, city, email, telephone):
    return print(
        f'{name} {surname}, {year} г., г.{city}, {email}, {telephone}')


get_info(name='Василий', surname='Вакуленко', city='Ростов-на-Дону',
         year=1980, telephone='88001112233', email='basta@mail.ru')
