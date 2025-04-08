
'''
Name: is_prefix
Input: two strings: pre_st (potential prefix) and st (main string)
Output: True or False
Algoritm: if the length of pre_st is 0, return False
if length of st is less than length of pre_st, return False
if the first character of pre_st and st do not match, return False
If pre_st has only one character left, return True
If the first characters match, call is_prefix(pre_st[1:], st[1:]) to compare the rest of the strings
'''
def is_prefix(pre_st, st):
    s_l = len(pre_st)
    b_l = len(st)
    if s_l == 0:  
        return False
    if b_l < s_l:
        return False
    if st[0]  != pre_st[0]:
        return False
    if len(pre_st) == 1:
        return True
    if st[0]  == pre_st[0]:
        return True and is_prefix(pre_st[1:], st[1:])
'''
Name: main function
Input: a string from user and pre_string from user also
Output: prints whether pre_st is a prefix of st or not
Algoritm: accept two strings
send the strings to is_prefix function
print the answers
'''    
def main():
    st = input("Enter a string: ")
    pre_st = input("Enter another string: ")
    if is_prefix(pre_st, st) == True:
        print((pre_st)," is a prefix of ",(st))
    else:
        print((pre_st)," is not a prefix of ",(st))
main()
    