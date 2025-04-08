'''
Name: check_str
Input: string
Output:True or False
Algoritm: if the string is empty (len(string) == 0), it is considered legal, returns True
check if the first character is outside the range of a-z or A-Z. If true, return False
If the first character is valid, make a recursive call to check the rest of the string (string[1:])

'''
def check_str(string):
    if len(string) == 0:
        return True
    if not (string[0] >= 'a' and string[0] <= 'z' or string[0] >= 'A' and string[0] <= 'Z') and check_str(string[1:]):
        return False
    return check_str(string[1:])
'''
Name: main function
Input:a string from user
Output: prints the answers
Algoritm: ask auser to input a string
call a check_string function
print  the answer
'''
def main():
    st = input("Please enter a string: ")
    if check_str(st) == True:
        print("The string is legal")
    else:
        print("The string is illegal")
main()