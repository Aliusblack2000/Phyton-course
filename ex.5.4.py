def average (num1,num2):
    average = ((num1+num2)/2)
    print("The average is: %.1f."%average, end= " ")
    if average%1 == 0:
        print("It is an integer number.")
    else:
        print("It is not an integer number")
    

def  multiplication (num1, num2):
    mult = num1*num2
    print("The multiplication is: %d"%(mult))

def minimum (num1, num2):
    if num1>num2:
        print("The minimum is: %d"%(num2))
    else:
        print("The minimum is: %d"%(num1))

def maximum (num1, num2):
   if num1>num2:
       print("The maximum is: %d"%(num1))
   else:
       print("The maximum is: %d"%(num2))

def power (num1, num2):
    if num2 > 0:
        answer = float(num1**num2)
        print("%d^%d is: %.2f"%(num1, num1, answer))
    else:
        print("Dividing by zero error")

def main():
    operation = 0
    while operation != "q" and operation != "Q" :
        print("\nOperations Menu: ")
        print("a or A : average: ")
        print("* : multiplication ")
        print("m : minimum")
        print("M: maximum")
        print(("^: power"))
        print("q or Q: quit")
        operation = input("\nEnter a character: ")
        if operation != "q" and operation != "Q":
            print("Enter two integer numbers.")
            f_integer = int(input("Enter the first integer: "))
            s_integer = int(input("Enter the second integer: "))
            if operation == "a" or operation == "A":
                average(f_integer,s_integer)
            elif operation == "*":
                multiplication(f_integer,s_integer)
            elif operation == "m":
                minimum(f_integer,s_integer)
            elif operation == "M":
                maximum(f_integer,s_integer)
            elif operation == "^":
                power(f_integer, s_integer)
    print("Finish")          


main()    