def main ():
    count_of_divisors = 0
    num = int(input(" Enter natural number: "))
    if num <= 0:
        print("Input is not a natural number")
        print()
    else:  
        right = 0
        
        print("The list of natural divisors of %d is: "%(num), end = " ")
        for i in range(1, num + 1):
            right = num%i
            if right == 0:
                count_of_divisors +=1
                print(i, end= " ")
        print("\nThe amount of divisors is: ",(count_of_divisors))
 
main()