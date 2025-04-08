def main():
    num = int(input("Enter a natural number: "))
    triangle_num = 0
    for i in range (1,num + 1):
        triangle_num += i
    print("The triangle number in location %d is: %d"%(num, triangle_num))
   
main()