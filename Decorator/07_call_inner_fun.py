# closures in python
def outer() -> None:
    def inner() -> None:
        print("Inside inner")
        x = 200
        return x
    return inner


inner = outer()
# After executing line 10 garbage collector clean memory for outer call
print(inner())
