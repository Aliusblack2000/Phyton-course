def main():
    a1 = int(input("Enter the first element in a geometric sequence: "))
    q = int(input("Enter the quotient of a geometric sequence: "))
    n = int(input("Enter an index / position in a sequence - a natural number: "))
    a = a1
    print("The first %d elenents in the sequence are: "%(n))
    for i in range(1, n+1):
        print(a,end=" ") 
        a = a1*(q**i) 
main()    