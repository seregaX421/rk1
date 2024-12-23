a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 > b1 or a1 > b2:
    print('пустое множество')
elif a1 <= a2 < b1:
    if b2 >= b1:
        print(a2, b1)
    elif b2 < b1:
        print(a2, b2)
elif a2 <= a1 < b2:
    if b1 >= b2:
        print(a1, b2)
    elif b1 < b2:
        print(a1, b1)
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(a1)