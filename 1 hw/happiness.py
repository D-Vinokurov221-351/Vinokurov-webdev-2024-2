n1 = int(input("Введите n1: "))
n2 = int(input("Введите n2: "))

arr = []

for i in range(n1):
    print("Insert " , i , " n: ", end ="")
    a = int(input())
    arr.append(a)

arr1 = []
arr2 = []
for i in range(n2):
    print("Insert " , i , " b: ", end ="")
    b = int(input())
    print("Insert " , i , " c: ", end ="")
    c = int(input())
    arr1.append(b)
    arr2.append(c)
    
ans = 0

for i in range(n1):
    for j in range(n2):
        if (arr[i] == arr1[j]):
            ans += 1
        if (arr[i] == arr2[j]):
            ans -= 1

print(ans)