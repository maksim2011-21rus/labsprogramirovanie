import numpy as np
import scipy
from scipy.linalg import solve

def Output(A, B):
    for row in range(len(A)):
        print('(', end='')
        for col in range(len(A[0])):
            print(f'{A[row][col]}', end=' ')
        print(f') * (x{row + 1}) = ({B[row]})')
    print('.' * 35)
def RowSwap(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]
def RowDivide(A, B, row, divider):
    if divider != 0:
        A[row] = [a / divider for a in A[row]]
        B[row] /= divider
    else:
        RowSwap(A, B, row, row + 1)
def RowSum(A, B, row, source_row, coefficient):
    A[row] = [(a + k * coefficient) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * coefficient
def Gauss(A, B):
    column = 0
    while column < len(B):
        RowDivide(A, B, column, A[column][column])
        Output(A, B)
        for i in range(len(A) - 1 - column):
            RowSum(A, B, i + 1 + column, column, -A[i + 1 + column][column])
        Output(A, B)
        column += 1
    print('Метод Гаусса:')
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    for i in range(len(X)):
        print(f'x{i + 1} = {round(X[i], 2)}')
def scipy_realization(myA, myB):
    print('Проверка через библиотеку SciPy:')
    X = solve(myA, myB)
    for i in range(len(X)):
        print(f'x{i + 1} = {X[i]}')
def makeTrianglePivot(A):
    for nrow in range(len(A)):
        pivot = nrow + np.argmax(abs(A[nrow:, nrow]))
        if pivot != nrow:
            A[nrow], A[pivot] = A[pivot], np.copy(A[nrow])
        row = A[nrow]
        divider = row[nrow]
        if abs(divider) < 1e-10:
            raise ValueError("Матрица несовместна")
        row /= divider
        for lower_row in A[nrow + 1:]:
            factor = lower_row[nrow]
            lower_row -= factor * row
    return A
def makeIdentity(A):
    for nrow in range(len(A) - 1, 0, -1):
        row = A[nrow]
        for upper_row in A[:nrow]:
            factor = upper_row[nrow]
            upper_row[-1] -= factor * row[-1]
            upper_row[nrow] = 0
    return A
def OutputNumpy(A):
    m1 = makeTrianglePivot(np.copy(A))
    m2 = makeIdentity(m1)
    roots = m2[:, -1]
    print('Проверка через Numpy:')
    for i in range(len(roots)):
        print(f'x{i + 1} = {roots[i]}')
def main():
    myA = [[-7.0, -9.0, 1.0, -9.0], [-6.0, -8.0, -5.0, 2.0], [-3.0, 6.0, 5.0, -9.0], [-2.0, 0.0, -5.0, -9.0]]
    myB = [29.0, 42.0, 11.0, 75.0]
    myA_sc = np.array([[-7, -9, 1, -9], [-6, -8, -5, 2], [-3, 6, 5, -9], [-2, 0, -5, -9]], float)
    myB_sc = np.array([29, 42, 11, 75], float).reshape((4, 1))
    myA_num = np.array([[-7, -9, 1, -9], [-6, -8, -5, 2], [-3, 6, 5, -9], [-2, 0, -5, -9]], float)
    Gauss(myA, myB)
    OutputNumpy(myA_num)
    scipy_realization(myA_sc, myB_sc)

if __name__ == "__main__":
    main()