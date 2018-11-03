import numpy as np

print("\n")
print("We are making the program for the multiplication of two matrices.")
print("\n")
valid_order= True
while valid_order:

    print("what should be the order of matrix A?\n")
    a_rows=int(input('enter the no of rows: '))
    a_columns=int(input('enter the no of columns: '))
    print("what should be the order of matrix B?")
    b_rows = int(input('enter the no of rows: '))
    b_columns = int(input('enter the no of columns: '))
    print("\nChecking whether the multiplication of these matrices is possible OR not....\n")
    if (a_columns == b_rows):
        print("Multiplication is possible")
        valid_order = False
    else:
        print("you entered the wrong order. Try again...")

a_mat=[]
print("Entries of elements of matrix A")
for i in range(a_rows):
    a_mat.append([])
for i in range(a_rows):
    for j in range(a_columns):
        a_mat[i].append(j)
        print('entry in row',i+1,'entry in column:',j+1)
        a_mat[i][j]=int(input())
print(a_mat)



b_mat = []
print("Entries of elements of matrix B")
for i in range(b_rows):
    b_mat.append([])
for i in range(b_rows):
    for j in range(b_columns):
        b_mat[i].append(j)
        print('entry in row', i + 1, 'entry in column:', j + 1)
        b_mat[i][j] = int(input())
print(b_mat)

r_mat = []
for i in range(a_rows):
    r_mat.append([])
for i in range(a_rows):
    for j in range(b_columns):
        r_mat[i].append(j)
        r_mat[i][j] = 0
print(len(r_mat))
print(".........Multiplying........")
for i in range(a_rows):
    for j in range(b_columns):
        for k in range(b_rows):
            r_mat[i][j] += a_mat[i][k] * b_mat[k][j]
print('the result is: '+str(r_mat))










