import random


def build_matrix(rows, cols):
    matrix = []
    for r in range(0, rows):
        matrix.append([random.randrange(0, 2, 1) for _ in range(0, cols)])
    print(matrix)


if __name__ == '__main__':
    build_matrix(6, 10)


def fibonacci_generator(n):
    j, k = 0, 1
    matrix = []
    for i in range(n):
        yield j
        yield k
        j, k = j + 1, k + 1
        # j = j + 1
        matrix.append([j for k in range(0, n)])

    print(matrix)


if __name__ == '__main__':
    fibonacci_generator(5)
