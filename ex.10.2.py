'''
Name: is_palindrom
Input: lst - the list of integers
Output: True or False
Algoritm: if a list has one or zero elements, it is a palindrome 
and Function returns True
If the first and last elements are not the same , return False
Recursia: checks the rest of the list with slizing lst[1-1] 
and calling recursive function again 
'''
def is_palindrom(lst):
    l = len(lst)
    if l <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_palindrom(lst[1:-1])
'''
Name: main function
Input: sequence of natural numbers,end with 0 from the user
Output: if it is 0 , so finish. if not so for each number prints if
it is palindrom or not
Algoritm: for each number converting it to string
convert the digits back to integers and store them in a list
pass the list to useful function is_palindrom
print the unswers
because of using the loop it will do it again until the user will not input 0

'''

def main():
    print("Enter a sequence of natural numbers,end with 0: ")
    num = int(input()) 
    while num != 0:
        lst = [] 
        for i in str(num):
            lst.append(int(i))
        if is_palindrom(lst) == True:
            print("The list of digits is a Palindrom")
        else:
            print("The list of digits is not a Palindrom")
        num = int(input())
    print("Finish")   
main()
      