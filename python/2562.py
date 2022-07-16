ls = []
for i in range(9):
    ls.append(int(input()))
max = max(ls)
for j in range(9):
    if ls[j] == max:
        index = j+1
print(max)
print(index)