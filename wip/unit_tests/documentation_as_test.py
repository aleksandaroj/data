class Stack:
    """
    Basic Stack implementation.

    :This class is used to check how automated testing and automated documentation works:

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.peek()
    2
    >>> stack.is_empty()
    False
    >>> stack.size()
    2
    >>> stack.pop()
    2
    >>> stack.pop()
    1
    >>> stack.is_empty()
    True
    >>> stack.size()
    0
    >>> stack.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty list
    """

    def __init__(self):
        """

        :This function takes one parameter:

        :param: self
                        Using this to access the attributes
        """
        self.items = []

    def push(self, item):
        """

        :Dokumentacija za push():
        :param item: x
        :return: x
        """
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not bool(self.items)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
