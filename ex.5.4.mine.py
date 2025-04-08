
def average(num1,num2):
    average = 0
    average = ((num1 + num2)//2)
    if average%1 != 0:
        print("The average is: ", average, "It is not an integer number.")
    else:
        print("The average is: %d"%(average))
    return average
def multiplication(num1,num2):
    m = 0
    m = num1 * num2
    return m
def minimum(num1,num2):
    a = 0
    if num1 > num2:
        a = num2
        print(a)
    else:
        a = num1
        print(a)
    return a 
def maximum(num1,num2):
     b = 0
    if num1 > num2:
        b = num1
        print(b)
    else:
        b = num2
        print(b)
    return b 
def power(num1,num2):
    if num2 = 0:
        print("Dividing by zero error")
    else:
        dividing = num1**num2
        print(dividing)
    return dividing
def main():
    int(input("a = "))
    int(input("b = "))
    print()    