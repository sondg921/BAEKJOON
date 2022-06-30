def yfunc():
    y = int(input())
    if y%4 == 0 and y%100 != 0:
        return 1
    elif y%400 == 0:
        return 1
    else:
        return 0

print(yfunc())