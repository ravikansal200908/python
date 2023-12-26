a = 50  # Global


def fun1() -> None:
    print('inside fun1')
    a = 10  # Local
    print(f'{a=}')
    print('Local namespace : ', dir())

    def fun2() -> None:
        print('inside fun2')
        b = 10  # Local
        print(f'{b=}')
        print('Enclosed namespace : ', dir())

    fun2()


print('Global namespace : ', dir())
fun1()
