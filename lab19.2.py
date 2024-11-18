import pickle

students = {
    'Іванов': 175, 'Петров': 160, 'Сидоренко': 185, 'Ковальчук': 168, 
    'Шевченко': 178, 'Мельник': 155, 'Кравець': 180, 'Лисенко': 170, 
    'Бондар': 182, 'Гончар': 165, 'Гриценко': 190, 'Данилюк': 177, 
    'Шевчук': 172, 'Тимошенко': 174, 'Коваль': 160, 'Клименко': 158,
    'Ткаченко': 184, 'Остапенко': 179
}

Q = int(input("Введіть зріст (Q), щоб відфільтрувати учнів: "))

filtered_students = {name: height for name, height in students.items() if height > Q}

with open('hi.dat', 'wb') as file:
    pickle.dump(filtered_students, file)

with open('hi.dat', 'rb') as file:
    loaded_students = pickle.load(file)
    print("Учні зі зростом більше за", Q, "см:", loaded_students)
