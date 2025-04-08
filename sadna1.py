def main():
    a, b = eval(input("Enter two numbers "))
    operator = input("Enter operator ")
    if operator == '+':
        print(a+b)
    elif operator == '-':
        print(a-b)
    elif operator == '*':
        print(a*b)
    elif operator == '/':
        if b == 0:
            print("error, try again")
        else:
            print(a/b)






main()    