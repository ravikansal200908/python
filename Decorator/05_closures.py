def outer() -> None:
    print('Inside outer')
    print('Hello')

    def inner() -> None:
        print('Inside inner')
        print('World')
    inner()


print(outer)  # It will print address
print(type(outer))  # It will print class
# inner()  # It show error because we can not call nested function directly
outer()

'''
- Closure is a technique by which data gets attached to the code.
- It remember values in the enclosing scope
- even if they are not present in the memory
- Follow 07_call_inner_fun.py
'''
