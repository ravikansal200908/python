class Decorator(object):
    def __init__(self, func) -> None:
        self.function = func

    def __call__(self, a, b) -> int:
        result = self.function(a, b)
        return result**2


@Decorator
def add(a, b):
    return a+b


print(f'{add(2, 3)=}')

# add = Decorator(add)
# print(f'{add(7, 3)=}')




