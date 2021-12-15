# function solution
def even_integers_function(_):
    result = []
    for i in range(_):
        if i % 2 == 0:
            result.append(i)
        return result


# generator solution
def even_integers_generator(i):
    for i in range(i):
        if i % 2 == 0:
            yield i


for n in even_integers_generator(10):
    print(n)


def fibonacci_generator(x):
    j, k = 0, 1
    for i in range(x):
        yield j
        j, k = k, j+k


for n in fibonacci_generator(10):
    print(n)


# if __name__ == '__main__':
#    even_integers_generator(10)
#    list(even_integers_generator(10))
