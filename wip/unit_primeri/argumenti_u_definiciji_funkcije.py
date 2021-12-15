def funk(err: list, x: int = None, options: dict = None):
    x = x if x is not None else len(err)
    print(x)


funk([1, 2, 3])

funk([1, 2, 3], x=7)
