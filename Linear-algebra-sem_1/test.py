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


def matrix_multiply(matrix, matrix2):
    new_matrix = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix))]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            for k in range(len(matrix[0])):
                new_matrix[i][j] += matrix[i][k] * matrix2[k][j]
    return new_matrix


P = open("input.txt", 'r')
M = open("output.txt", 'w')
stop = 0
st = P.readline()
alpha, beta = map(float, st.split())
st = P.readline()
na, ma = map(int, st.split())
st = P.readline()
a = list(map(float, st.split()))
a_matrix = create_matrix(na, ma, a)
st = P.readline()
nb, mb = map(int, st.split())
st = P.readline()
b = list(map(float, st.split()))
b_matrix = create_matrix(nb, mb, b)
st = P.readline()
nc, mc = map(int, st.split())
st = P.readline()
c = list(map(float, st.split()))
c_matrix = create_matrix(nc, mc, c)
st = P.readline()
nd, md = map(int, st.split())
st = P.readline()
d = list(map(float, st.split()))
d_matrix = create_matrix(nd, md, d)
st = P.readline()
nf, mf = map(int, st.split())
st = P.readline()
f = list(map(float, st.split()))
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
    M.write('1' + '\n')
    M.write(str(len(x_matrix)) + ' ' + str(len(x_matrix[0])) + '\n')
    for i in range(len(x_matrix)):
        for j in range(len(x_matrix[0])):
            M.write(str(x_matrix[i][j]) + ' ')
        M.write('\n')
else:
    M.write('0')
P.close()
M.close()
