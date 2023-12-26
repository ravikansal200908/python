'''
- objects which can be called whenever required
- objects having __call__() method in their class
'''

x = 100
name = 'test'


def add(a, b) -> int:
    return a+b


print(f'{type(add)=}')
print(f'{callable(x)=}')
print(f'{callable(name)=}')
print(f'{callable(add)=}')

print(add(10, 20))
print(add.__call__(10, 20))
