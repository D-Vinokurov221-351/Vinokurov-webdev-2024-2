import csv

child = 0.0
adult = 0.0
pens = 0.0


with open("products.csv", encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        child += float(row["Ребенок"])
        adult += float(row["Взрослый"])
        pens += float(row["Пенсионер"])
    print("child =" , round(child, 2) , "\nadult =" , round(adult, 2) , "\npensioner =" , round(pens, 2))