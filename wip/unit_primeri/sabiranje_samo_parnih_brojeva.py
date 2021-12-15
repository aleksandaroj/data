# Sabiranje samo parnih brojeva u nizu

niz = [1, 2, 4, 4, 5, 6, 7, 8, 10]


def sumeven(dataset):
    x = 0
    idx = 0
    while idx < len(dataset):
        if dataset[idx] % 2 == 0:
            x += dataset[idx]
        idx += 1
    print(x)


print(niz)
sumeven(niz)
