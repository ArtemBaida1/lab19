import shelve

students = {
    'Іванов': 175, 'Петров': 160, 'Сидоренко': 185, 'Ковальчук': 168, 
    'Шевченко': 178, 'Мельник': 155, 'Кравець': 180, 'Лисенко': 170, 
    'Бондар': 182, 'Гончар': 165, 'Гриценко': 190, 'Данилюк': 177, 
    'Шевчук': 172, 'Тимошенко': 174, 'Коваль': 160, 'Клименко': 158,
    'Ткаченко': 184, 'Остапенко': 175
}

Q = int(input("Введіть зріст (Q), щоб відфільтрувати учнів: "))

with shelve.open('hi.dat') as db:
    for name, height in students.items():
        if height > Q:
            db[name] = height

print("\n")
print("Дані про учнів зі зростом більше за", Q, "см було записано у файл.")

with shelve.open('hi.dat') as db:
    print("\n")
    print("Учні зі зростом більше за", Q, "см:")
    for name in db:
        print(f"{name}: {db[name]} см")
