from random import randint
def find_biggest(rec):
    rows = len(rec)    # 3 rows in your example
    cols = len(rec[0])

def make_rand_matrix(rows, cols):
    matrix = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = randint(0, 1)
    return matrix

rows = 7
cols = 7
matrix = make_rand_matrix(rows, cols)
for i in matrix:
    for j in i:
        print (j, end="  ")
    print ('\n')
