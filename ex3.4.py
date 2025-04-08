def main ():
    num=int(input("Please enter 4-digits integer: "))
    pair1 = num%100
    pair2 = num//100
    print ("New number: %1d"%(pair1*100+pair2))
    n1=(pair1//10)%2
    n2=pair1%2
    n3=(pair2//10)%2
    n4=pair2%2    
    even=4-(n1+n2+n3+n4)
    print("The amount of even digits in the number %d is %d"%(num, even))    
main()
    
