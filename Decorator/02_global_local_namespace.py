a = 50  # Global


def fun1() -> None:
    print('inside fun1')
    a = 10  # Local
    print(f'{a=}')
    print('Local namespace : ', dir())


def fun2() -> None:
    print('inside fun2')
    a = 10  # Local
    print(f'{a=}')
    print('Local namespace : ', dir())


print('Global namespace : ', dir())
fun1()
fun2()
