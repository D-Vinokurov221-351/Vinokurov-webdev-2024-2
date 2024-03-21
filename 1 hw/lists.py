n = int(input("Введите n: "))
arr = list()
for j in range(n):
    print("Введите ", j, " действие: ")
    do = str(input())
    if (do == "insert"):
        e = int(input("Введите e: "))
        i = int(input("Введите i: "))
        arr.insert(i, e)
    if (do == "print"):
        print(arr)
    if (do == "remove"):
        e = int(input("Введите e: "))
        arr.remove(e)
    if (do == "append"):
        e = int(input("Введите e: "))
        arr.append(e)
    if (do == "sort"):
        arr.sort()
    if (do == "pop"):
        arr.pop()
    if (do == "reverse"):
        arr.reverse()
