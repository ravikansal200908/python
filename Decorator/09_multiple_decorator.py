def decor1(func):
    def inner():
        return func().upper()
    return inner


def decor2(func):
    def inner():
        return func().split()
    return inner


@decor2  # Execute second
@decor1  # Execute first
def getName():
    f_n = "test"
    l_n = "user"
    name = f_n+" "+l_n
    return name


# getName = decor2(decor1(getName))
print(getName())
