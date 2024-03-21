
n = float(input())
m = int(input())

items = []

for i in range(m):
    s = str(input())
    v = float(input())
    c = float(input())
    
    itemInfo = {
        'cpv': c / v,
        'c': c,
        'v': v,
        's': s
    }
    
    if len(items) == 0:
            items.append(itemInfo)
    else:
        k = 0
        while k < len(items) and items[k]['cpv'] > itemInfo['cpv']:
            k += 1
        items.insert(k, itemInfo)

total = 0
for item in items:
    if n - item['v'] >= 0:
        n -= item['v']
        print(item['s'] , " " , int(item['v']) , " " , int(item['c']))
    elif n > 0:
        print(item['s'] , " " , round(n / item['v'], 2) , " " , round(n / item['v'] * item['c'], 2))
        break

