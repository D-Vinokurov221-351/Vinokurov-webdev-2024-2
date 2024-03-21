n = int(input("Введите n: "))
arr = []
arr1 = []
for i in range(n):
    print("Введите a: ")
    a = int(input())
    print("Введите b: ")
    b = int(input())
    arr.append(a)
    arr1.append(b)
t = int(input("Введите t: "))


ans = 0
for i in range(n):
    if (t <= arr1[i] and t >= arr[i]):
        ans += 1

print(ans)