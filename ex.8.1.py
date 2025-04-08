'''
combined string function
input string 1, string 2 and index x
output new string
algoritm:
    I am making a new empty string
    every small letter i am making big 
    for this i am using Askiy table
    them i am using a new string to safe big letters
    and making sum of strings
'''
def combineStr(s1,s2,x):
    new_s = ''
    for i in s2:
        if i >= 'a' and i <= 'z':
            i = ord(i) - 32
            new_s += chr(i)
    return print(s1[:x] + new_s + s1[x:])
'''
main function
asking a user to put in 2 strings and index
then I am checking wether index is possible for the first string
If it is possible I am usinh combine function
printing an answer
'''
def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    x = int(input("Enter index x: "))
    if x < 0 or x > len(s1):
        print("Invalid index")
    else:
        print("combined string ")
        combineStr(s1, s2, x)
main()
    