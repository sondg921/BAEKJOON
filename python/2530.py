A, B, C = map(int, input().split())
D = int(input())
E = C + D
if E >= 60:
    E = E % 60
    B = B + (C + D)//60
if B >= 60:
    A = A + (B//60)
    B = B % 60
if A >= 24:
    A = A % 24
print(A,B,E)
