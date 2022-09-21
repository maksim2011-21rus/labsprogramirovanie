import sys

epsilon = 0.01

class MatrixError(Exception):
    pass

class MethodError(Exception):
    pass


def zendel_method(alpha_norma, beta, alpha):
    x_old = beta.copy()
    x_new = [0 for _ in range(len(beta))]
    epsilon_k_fst = 1
    cnt_iteration = 0
    while True:
        x_new = [0 for _ in range(len(beta))]
        for i in range(len(alpha)):
            for j in range(len(alpha[0])):
                if j < i:
                    x_new[i] += alpha[i][j] * x_new[j]
                else:
                    x_new[i] += alpha[i][j] * x_old[j]
            x_new[i] += beta[i]

        diffence_of_x = 0
        for i in range(len(beta)):
            diffence_of_x = max(abs(x_new[i] - x_old[i]), diffence_of_x)
        epsilon_k = epsilon_k_fst * diffence_of_x
        if epsilon_k <= epsilon:
            break
        cnt_iteration += 1

        x_old = x_new.copy()
    print("Метод Зенделя:")
    print([round(i, 2) for i in x_new])
    print("Итераций = {}".format(cnt_iteration))


def simple_iterations_aux(alpha_norma, beta, alpha):
    x_old = beta.copy()
    x_new = [0 for _ in range(len(beta))]
    epsilon_k_fst = 1
    cnt_iteration = 0
    while True:
        x_new = [0 for _ in range(len(beta))]
        for i in range(len(alpha)):
            for j in range(len(alpha[0])):
                x_new[i] += alpha[i][j] * x_old[j]
            x_new[i] += beta[i]

        diffence_of_x = 0
        for i in range(len(beta)):
            diffence_of_x = max(abs(x_new[i] - x_old[i]), diffence_of_x)
        epsilon_k = epsilon_k_fst * diffence_of_x
        if epsilon_k <= epsilon:
            break
        cnt_iteration += 1

        x_old = x_new.copy()
    print("Простые итерации:")
    print([round(i, 2) for i in x_new])
    print("Итераций = {}".format(cnt_iteration))


def simple_iteraions(matrix, b):
    n = len(matrix)
    alpha = [[0 for _ in range(n)] for _ in range(n)]
    beta = [0 for _ in range(n)]
    for i in range(n):
        aii = matrix[i][i]
        beta[i] = b[i] / aii
        for j in range(n):
            if i != j:
                alpha[i][j] = -(matrix[i][j] / aii)

    alpha_norma = 0
    for i in range(len(alpha)):
        tmp = 0
        for j in range(len(alpha[0])):
            tmp += abs(alpha[i][j])
        alpha_norma = max(tmp, alpha_norma)

    simple_iterations_aux(alpha_norma, beta, alpha)
    print()
    zendel_method(alpha_norma, beta, alpha)


def main():
    matrix = [[12, -3, -1, 3], [5, 20, 9, 1],[6, -3, -21, -7], [8, -7, 3, -27]]
    b = [-31, 90, 119, 71]
    print("epsilon = {}\n".format(epsilon))
    simple_iteraions(matrix, b)


if __name__ == "__main__":
    main()