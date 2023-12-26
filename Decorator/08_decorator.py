'''
- adding things to something to make more attractive/presentable
- it take another function as input, add additional functionality and return it
- it's a callable object which modifies other function/class

'''


def decor(func):

    def inner():
        print('Before execution.')
        func()  # existing functionality
        print('After execution.')

    # inner()
    return inner


@decor
def printer():
    print('Inside printer function')
    print('Welcome')


# decor(printer)

# printer = decor(printer) or @decor
printer()
