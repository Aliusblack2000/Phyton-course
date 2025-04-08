def main():
    a, b, c = eval(input("Please insert triangle sides: "))
    print("a = %.1f, b = %.1f, c = %.1f"%(a, b, c))
    print("Perimeter = %.3f"%(a+b+c))
    print("Area = %.3f"%((((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**.5))
    
main ()