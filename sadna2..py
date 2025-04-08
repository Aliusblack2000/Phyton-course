
def check_sum(a, sum1):
    if len(a) == 0:
        if (sum1 == 0):
            return True
        else:
            return False
    else:
        return check_sum(a[1:], sum1) or check_sum(a[1:], sum1 - a[0])





'''
def power_rec(a,n): #סיבוכיות O(n)
    if n == 0:
        return 1 
    return a * power_rec(a, n-1)

def power_rec(a,n): #סיבוכיות log(n)
    if n == 0:
        return 1 
    if n == 1:
        return a
    temp = power_rec(a, n//2)
    if n%2 == 0:
        return temp * temp
    return temp*temp*2

def fun1(num):
    ret = 0
    if num > 10:
        if (num%10 == (num//10)%10):
            ret = 1 
        ret += fun1(num//10)
    return ret

def pr(string):
    if len(string) == 0 :
        return True
    toprint = pr(string[1:])
    if (toprint):
        print(string[0])
    return not toprint
pr('abcde')
'''