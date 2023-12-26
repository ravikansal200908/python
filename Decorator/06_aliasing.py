def outer() -> None:
    print("Hello")

    def inner() -> None:
        print("Bye")
    inner()


# creating alias
new_fun = outer

new_fun()
outer()
