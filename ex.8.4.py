'''
separate
input a string from main function
outpur a string every word from a new line
going through the list and looking for words
If there is empty space or tub so this is a new word from another line 
'''
def separate(lst):
    for i in  range (len(lst)):
        if lst[i] != ('\t') and lst[i] != (' '):
            print(lst[i], end= '')
        else:
            print()
'''
main function
asking a user to enter a string
it calls for separate function
until we don't have empty list we are asking a user to write a string once again
if the list is empty(Enter) the program will be finished
'''
def main():
    lst = []
    while lst != '' :
        lst = input("Enter a string, please: ")
        separate(lst)
        print()
    print("Finish")
main()