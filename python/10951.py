import sys
try:
    while True:
        a,b = map(int,input().split())
        print(str(a+b))
except :
    sys.exit