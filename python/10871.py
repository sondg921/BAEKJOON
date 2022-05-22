N, X = map(int,input().split())
A = input().split()
list = []
for i in range (N):
    if int(A[i]) < X :
        list.append(A[i])
    else :
        pass
for k in range (len(list)):
    print(list[k], end=' ')
