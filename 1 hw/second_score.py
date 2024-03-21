n = int(input("Введите n: "))
set1 = set()
for i in range(n):
    print("Введите", i, "значение: ", end="")
    a = int(input())
    set1.add(str(a))
print(sorted(set1)[-2])
