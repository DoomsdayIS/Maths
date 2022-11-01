
def create_matrix(n, m, values):
    new_matrix = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            new_matrix[i][j] = values[i * m + j]
    return new_matrix


def multiply_const_matrix(const, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = const * matrix[i][j]
    return matrix


def trans(matrix):
    new_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def matrix_sum(matrix, matrix2):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += matrix2[i][j]
    return matrix


def matrix_multiply(matrix,matrix2):
    new_matrix = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix))]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            for k in range(len(matrix[0])):
                new_matrix[i][j] += matrix[i][k]*matrix2[k][j]
    return new_matrix


alpha, beta = map(float, input().split())
na, ma = map(int, input().split())
a = list(map(float, input().split()))
a_matrix = create_matrix(na, ma, a)
nb, mb = map(int, input().split())
b = list(map(float, input().split()))
b_matrix = create_matrix(nb, mb, b)
nc, mc = map(int, input().split())
c = list(map(float, input().split()))
c_matrix = create_matrix(nc, mc, c)
nd, md = map(int, input().split())
d = list(map(float, input().split()))
d_matrix = create_matrix(nd, md, d)
nf, mf = map(int, input().split())
f = list(map(float, input().split()))
f_matrix = create_matrix(nf, mf, f)
if ma == nb and na == mb and mc == ma and na == nd and nf == nc and md == mf:
    a_matrix = multiply_const_matrix(alpha, a_matrix)
    b_matrix = trans(b_matrix)
    b_matrix = multiply_const_matrix(beta, b_matrix)
    ab_matrix = matrix_sum(a_matrix, b_matrix)
    ab_matrix = trans(ab_matrix)
    abc_matrix = matrix_multiply(c_matrix, ab_matrix)
    x_matrix = matrix_multiply(abc_matrix, d_matrix)
    f_matrix = multiply_const_matrix(-1,f_matrix)
    x_matrix = matrix_sum(x_matrix, f_matrix)
    print(1)
    print(len(x_matrix), len(x_matrix[0]))
    for i in range(len(x_matrix)):
        print(*x_matrix[i])
else:
    print(0)




