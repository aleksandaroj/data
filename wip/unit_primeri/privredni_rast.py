def privredni_rast():
    y = 100
    for x in range(10):
        y = y * 1.07
        # print(x, y)
    return y


print(privredni_rast())
