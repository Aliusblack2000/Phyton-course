'''
function perfect
input matrix
output wether the matrix is perfect or not
algoritm:
    i am cheking every row to ensure all numbers from 1 to len of matrix
    i am using a boolean list dim size to check wich numbers were there twise and more
    similary i am checking each column
    
'''
def perfect(mat):
    flag = True
    dim = len(mat)
    for r in mat:
        counter = [False]*dim
        for num in r:
            if num < 1 or num > dim or counter[num - 1] == True:
                return False
            counter[num - 1] = True
    
    for c in range (dim): 
        counter = [False]*dim
        for r in range(dim):
            num = mat[r][c]
            if num < 1 or num > dim or counter[num - 1] == True:
                return False
    return flag
'''
main function
i am asking a user to input a number of matrix dimension
also i am using a new parametr flag for not to use another loop
if the dimention of matrix is illegal the program stops 
if everything is ok i ask a user to enter rowwise
then i am building a matrix
i am printing a matrix
using the perfect useful function checking wether the matrix is perfect or not
until the user use legal dimention the program continios working/ 
'''
def main():
    flag = 1
    while flag != 0:
        dim = int(input("Enter the matrix dimension : "))
        if dim < 1:
            flag = 0
            return print("Finish")
        print("Enter the entries rowwise: ")
        mat = []
        for r in range(dim):
            new_mat = []
            for c in range(dim):
                new_mat.append(int(input()))
            mat.append(new_mat)
            
        for i in range(dim):
            for j in range(dim):
                print('%6i' %(mat[i][j]),end="")
            print()
        print()
        if perfect(mat) == True:
            print("The Matrix is perfect")
        else:
            print("The Matrix is not perfect" )
main()