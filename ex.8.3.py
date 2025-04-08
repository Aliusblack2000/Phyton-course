'''
removing_function
input: string (lst) from user
output: string (ls) without double units
algoritm: uses new empty list, going through users list and looking for double letters
then removing uniq letters into new list
'''
def removing_function(lst):
    ls = []
    for i in range (len(lst)):
        if lst[i:i+1] != lst[i-1:i]:
            ls.append(lst[i])
    return ls
'''
main function
asking a user to enter a string 
using function for removing repetition
printing a new list 
'''
def main():
    lst = input("Enter a string, please: ")
    ls = removing_function(lst)
    print("After removing all duplicates:", end='')
    for i in ls:
        print(i,end='')
main()