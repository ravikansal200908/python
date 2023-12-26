# LEGB --> Local, Enclosed, Global, Built-in
x = 100  # Global variable


def outer() -> None:
    x = 20  # Non-local variable

    def inner() -> None:
        nonlocal x
        x = x+20  # Local variable
        print(f'X in inner : {x}')
    inner()
    print(f'X in outer is : {x}')


outer()

'''
- At first it will check value in local-->non-local-->global-->built in-->error

|-Built-in----------------------|
|                               |
| |-Global--------------------| |
| |                           | |
| | |-Non-Local-------------| | |
| | |                       | | |
| | | |-Local-------------| | | |
| | | |                   | | | |
| | | |-------------------| | | |
| | |                       | | |
| | |-----------------------| | |
| |                           | |
| |---------------------------| |
|                               |
|-------------------------------|

- Variable checking rule would be inner to outer

'''
