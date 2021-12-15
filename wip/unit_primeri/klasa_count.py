class Count:
    def __init__(self, minimum, maksimum):
        self.min = minimum
        self.max = maksimum

    def __iter__(self):
        self.n = self.min - 1
        return self

    def __next__(self):
        if self.n == self.max:
            raise StopIteration
        self.n += 1
        return self.n


c = Count(1, 2)
# for i in c:
#     print(i)
