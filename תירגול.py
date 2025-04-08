





'''
def aN (a1, q, n):
    if n == 1:
        return a1
    return q * (aN(a1, q, n-1))
print(aN(3, 2, 4))

def func3(a,n):
    cnt = 1
    n -= 1
    if n > 0:
        cnt += func3(a[1:], n)
    print(a[0], end= ' ')
    return cnt
print(func3((123,456,789), 3))

def func2 (a,b):
    if a < b:
        return func2(a, b-a)
    return a-b
print(func2(82, 175))

def func1(a):
    if a > 9:
        return 1 + func1(a//10)
    return 1 
func1(732)
'''