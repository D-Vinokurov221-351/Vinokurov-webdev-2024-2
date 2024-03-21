s = str(input("Введите n: "))
arr = ['а','е','ё','и','й','о','у','э','ю','я','А','Е','Ё','И','Й','О','У','Э','Ю','Я']
sum1 = 0
sum2 = 0
for i in range(len(s)):
    isNotVowel = True
    for j in arr:
        if (j == s[i]):
            isNotVowel = False
            sum1 += len(s) - i
    if (isNotVowel):
        sum2 += len(s) - i
if (sum1 > sum2):
    print("Победил Кевин со счетом: " , sum1)
elif (sum1 == sum2):
    print("Ничья Кевина и Стюарта со счетом: " , sum1)
elif (sum1 < sum2):
    print("Победил Стюарт со счетом: " , sum2)