#changing the recursion limit
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1100)
print(sys.getrecursionlimit())
i=1
def d1():
    global i
    print('hello world',i)
    i+=1
    d1()
d1()