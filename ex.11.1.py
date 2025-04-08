'''
name: max num
input: the list of digits from def main
output: number
algoritm: first of all I want want to find an index
of a largest number. with use of lope i am taking
the index (I) like index of the biggest number
then I am using another lope which runs
through the list from index (I+1). if it is bigger
i am moving it to the orrect position by swappin
After sorting, it combines the digits into the 
largest possible number
Time Complexity: O(n^2) + O(n) = O(n^2)
Space Complexity: O(1)
'''
def max_num(lst):
    l = len(lst)
    num = 0
    for i in range(l):
        i_max = i
        for j in range(i + 1, l):
            if (lst[j] > lst[i_max]):
                i_max = j
        lst[i],lst[i_max] = lst[i_max],lst[i]
    for x in lst:
        num  = num*10 + x     
    return num 
'''
name: main
input: User input list of digits
output: Displays the largest number formed
algoritm:  Takes user input, appends digits to a list, and calls max_num() to return the largest number formed from the digits.
'''     
def main():
    ls = []
    print("Enter digits: ")
    num = 0
    while num != -1:
        num = int(input())
        if num != -1:
            ls.append(num)
    if len(ls) == 0 and num == -1:
        print("Input Error")
    else:
        print("The largest number is: ",max_num(ls))
main()