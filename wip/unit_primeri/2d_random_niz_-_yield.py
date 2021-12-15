

def fibonacci_generator(i):
    j, k = 0, 1
    matrix = []
    for _ in range(i):
        yield j
        yield k
        j, k = j + 1, k + 1
        matrix.append([j for k in range(0, i)])
    print(matrix)


for x in fibonacci_generator(3):
    print(x)
