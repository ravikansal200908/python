
class Add(object):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b


a1 = Add(10, 20)

print(f'{callable(Add)=}')
print(f'{callable(a1)=}')  # objects are not callable


class Add(object):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __call__(self) -> None:
        print('Inside __call__() method.')


a1 = Add(10, 20)
a1()
print(f'{callable(a1)=}')  # Now a1 is callable
