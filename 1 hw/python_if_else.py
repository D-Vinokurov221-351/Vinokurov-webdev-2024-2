n = int(input("Введите n: "))
if (n % 2 == 0) or (n % 2 == 1 and n >= 6 and n <= 20):
    print("Weird")
else:
    print("Not Weird")
