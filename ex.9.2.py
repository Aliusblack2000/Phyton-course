'''
name: is extreme
input: matrix
output: true or false
algorithm: its using the function check matrix to check whether it square or not
them i am looking for a length of matrix
i am making two lists where i am putting a numbers of two diagonals
then i am looking for maximum in diagonal minor and comparing it with minimum in diagonal main
then it returnss me whether the matrix is extreme or not
'''
def is_extreme(mat):
    Flag = check_matrix(mat)
    n = len(mat)
    diagonal_main = []
    diagonal_minor =[]
    for x in range (n):
       diagonal_main.append(mat[x][x])
       diagonal_minor.append(mat[x][n-x-1])
    maximum = diagonal_minor[0]
    minimum = diagonal_main[0]    
    for i in range (len(diagonal_minor)-1):
       if maximum < diagonal_minor[i]:
           maximum = diagonal_minor[i]
    for j in range (len(diagonal_main)-1):
       if minimum > diagonal_main[j]:
           minimum = diagonal_main[j]
    if minimum >= maximum:
       Flag = True
    else:
       Flag = False
    return Flag
'''
name: check matrix
input: matrix
output: True or False
algorithm: it is checking whether the matrix is squared or not
'''
def check_matrix(mat):
    row = len(mat)
    col = len(mat[0])
    if row != col:
        return False
    return True
    
def print_matrix(mat):
    for i in range (len(mat)):
        for j in range(len(mat[i])):
            print ("%5d"%mat[i][j], end='')
        print()
'''
name: main function
input: 4 matrixes
output: printing 4 matrixes and saying whether each of them is extreme or not
algorithm: example matrix one:
    printing the first matrix
    using a function to chack whether it is extreme or not by using True or False
    printing the answser
'''  
def main():
    print('first matrix:')
    m_1=[[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5]]
    print_matrix(m_1)
    print('is extreme matrix:',is_extreme(m_1)) 
    
    print('second matrix:')
    m_2=[[5,2,3,4,2],[6,7,8,3,0],[1,2,4,4,5],[1,2,3,4,5]]
    print_matrix(m_2)
    print('is extreme matrix:',is_extreme(m_2)) 
    
    
    print('third matrix:')
    m_3=[[5,2,3,4,2],[6,7,8,3,0],[1,2,4,4,5],[6,0,8,9,0],[1,2,3,4,5]]
    print_matrix(m_3)
    print('is extreme matrix:',is_extreme(m_3)) 
    
    
    print('fourth matrix:')
    m_4= [[1]]
    print_matrix(m_4)
    print('is extreme matrix:',is_extreme(m_4),end = '') 
main()
    
