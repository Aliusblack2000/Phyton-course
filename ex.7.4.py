def create_list(number):
    count = [0]*10
    if number < 0:
        number *= -1 
    if number == 0:
        count[0] = 1
    if number != 0:
        count[number%10] += 1
        number //= 10
    return count

def main():
    count = [0]*10 
    num = int(input("Enter integer: "))
    ls = create_list(num) 
    
    while num != 0:    
        for digit in ls:
            if digit in count:
                count[digit] +=1
            else:
                count[digit] = 1
                    
        for digit in count:
            print("The digit %d appears %d times"%(digit, count[digit]))
                    
        max_count = 0
        most_frequent = []
        for digit in count:
            if count[digit] > max_count:
                max_count = count[digit]
                most_frequent = [digit]
            elif count[digit] == max_count:
                most_frequent.append(digit)
            print("The most frequent digit/s is/are : ", most_frequent) 
            print("It occurs times %d"%(max_count))
main()        