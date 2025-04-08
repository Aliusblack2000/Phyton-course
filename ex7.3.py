def create_list(number):
    count = [0] * 10
    if number < 0:
        number *= -1  # Convert negative number to positive
    if number == 0:
        count[0] = 1  # Special case for 0
    while number != 0:
        count[number % 10] += 1
        number //= 10
    return count

def main():
    count = [0] * 10
    num = 1
    while num != 0:
        num = int(input("Enter integer: ")) 
        ls = create_list(num)
    
        for digit in range(len(ls)):
            if ls[digit] > 0:
                print("The digit %d appears %d times" % (digit, ls[digit]))
        
        max_count = 0
        most_frequent = []
        
        for digit in range(len(count)):
            if ls[digit] > max_count:
                max_count = ls[digit]
                most_frequent = [digit]
            elif ls[digit] == max_count and ls[digit] != 0:
                most_frequent.append(digit)
        print("The most frequent digit/s is/are: ", end= ' ')     
        for j in most_frequent:
            print (j, end= ' ')
        print()
        print("It occurs times %d\n" % max_count)

main()