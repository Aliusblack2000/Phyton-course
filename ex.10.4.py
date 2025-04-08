'''
Name:convert_num
Input: string   
Output: int
Algoritm: recursive function. First of all I want to do basic check 
if string is empty so return 0 (we don't have anything there)
then I am taking the first charecter of the string 
and for my comfy give it a name
then i am converting only the first character to its
numerical value
then i am calculating the value of the first digit based on its 
position
and i am using recursia to rewrite the rest of numbers of 
the string

'''
def convert_num(st):
    if len(st) == 0:
        return 0
    f_unit = st[0]
    unit = ord(f_unit) - ord('0')
    return unit*(10**(len(st)-1)) + convert_num(st[1:]) 
'''
Name:main function
Input:  string from user  
Output: answers
Algoritm: first of all i am checking if the string contains 
only digits with help of 'for x in str' which checks every 
digit in string
i use a flag to accept a use of loop in loop
if all characters are valuable i am using my convert_num function
and print the answers

'''

def main():
    string = input("Please enter a string:")
    Flag = True
    for x in string:
        if x < '0' or x > '9':
            Flag = False
    if Flag == True:
        print('The string "%s" corresponds to the number %d '%(string, convert_num(string)))
    else:
        print("The string is illegal!")
        
main()