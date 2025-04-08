


def group_lst(left, right):
    if len(right) == 0:
        return left
    left.append(right[0])
    return group_lst(left, right[1:])
'''
Name:into_list
Input:A sorted list of integers (lst) and single int
eger (number)
Output: A new sorted list containing all elements of `lst` and `num`
Algorithm:
i am checking a list. if list is empty i am containing
a new list with number
i am comparing the first unit of lst with number.
if num is smaller i am appending lst[0] and then using 
recursive function for the last part lst[1;]
end returning a new lst
'''
def into_list (lst, num):
    if len(lst) < 1:
        n_l = []
        n_l.append(num)
        return n_l
    if num <= lst[0]:
        n_l = []
        n_l.append(num)
        n_l.append(lst[0])
        return group_lst(n_l,lst[1:])
    n_l = []
    n_l.append(lst[0])
    rest_of_l = into_list(lst[1:], num)
    return group_lst(n_l, rest_of_l)


    



'''
Name: main function
Input: 5 integers from user and single integer for number
Output: answers
Algorithm: i am creating an empty list, asking a user
for 5 elements and the appending them into the list
printing the original list
asking a user for single number
and then using a function into_list to take a number
into the list on the right place
printing a new list
'''
def main():
    print("Enter elements: ")
    lst = []
    for x in range(5):
        x = int(input())
        lst.append(x)
    print("The List: ", (lst))
    print("Enter new number: ")
    num = int(input())
    print("The New List:", (into_list(lst, num)))
main()