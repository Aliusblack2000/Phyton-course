'''
cross sum
input matrix and index of row
output True or False
is going through one row and summing all of units
is telling us whether the sum of row equals the row
'''
def cross_sum(mat, row):
    sum_row = 0
    for i in range (len(mat[0])):
        sum_row = mat[row][i] + sum_row
        if sum_row == row:
            return True
    return False
'''
positive diagonal
input matrix
output True or False
going through diagonal of matrix andsaying us whether all numbers are possitive or not
'''
def positive_diagonal(mat):
    for i in range (len(mat)):
        if mat[i][i] <= 0:
            return False
    return True
'''
main function
asking a user for 25 numbers
making a matrix with these numbers 5*5
printing a matrix
using fuunctions and telling the user whether the matrix is legal or not
'''
def main():
    print("Please enter the matrix elements: ")
    mat = []
    flag = True
    for row in range(5):
        temp = []
        for col in range(5):
            temp.append(int(input()))
        mat.append(temp)
    print("The matrix is:")
    for b in range(len(mat)):
        if cross_sum(mat, b) != True:
            flag = False
        for i in mat[b]:
            print("%5d"%i, end='')
        print()
    if flag == False or positive_diagonal(mat) == False:
        return print("The matrix is illegal!")
    return print("The matrix is legal!")
main()
            
        