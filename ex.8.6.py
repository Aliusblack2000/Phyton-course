'''
most positive
input the matrix from main function
output the row with the lowwest index and with the biggest number of possitive units
is looking for the row that has the biggest number of positive numbers
if there is amount of rows that all numbers there are positive 
we are checking wich of them has the lowest index

'''
def most_pos(mat):
    big = 0
    i_max = 0
    for r in range(len(mat)):
        counter = 0
        for c in mat[r]:
            if c > 0:
                counter += 1
        if counter > i_max:
            i_max = counter
            big = r
    return big
'''
main fuction
asking the user to input a number of rows and cons
then to input a numbers to build a matrix
them we create a new matrix and print it
then we are using a function of most_pos to find the row with the most positive values
and we are printing its index
 
'''  
def main():
    num_of_rows = int(input("Enter number of rows: "))
    num_of_cols = int(input("Enter number of columns: "))
    mat = []
    print("Enter the matrix elements: ")
    for r in range(num_of_rows):
        temp = []
        for c in range(num_of_cols):
            temp.append(int(input()))
        mat.append(temp)
    print("The entered matrix is: ")
    for x in mat:
        print(x)
    print("The row with the most positive values is: %d"%most_pos(mat))
main()