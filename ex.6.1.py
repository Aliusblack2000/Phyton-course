def print_triangle(letter, integer):
    for i in range (integer , 0, -1):
        print(letter * i, end = " ")
        print()

def main():
    character = input("Enter a letter: ")
    number = int(input("Enter an integer: "))
    print(" *** Triangle *** ")
    print_triangle(character, number)
main()