n = int(input("Введите n: "))
records = list()
marks = set()
sorted_marks = list()
names = list()
for i in range(n):
    print("Введите ", i, " имя: ", end="")
    name = input()
    print("Введите ", i, " оценку: ", end="")
    score = float(input())
    records.append([name, score])
    marks.add(score)
sorted_marks = list(marks)
sorted_marks.sort()
for i in records:
    if (sorted_marks[1] == i[1]):
        names.append(i[0])
names.sort()
for i in names:
    print(i, end = "\n") 
