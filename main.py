main_number = (input('Input One number 1-3: '))
list = ['a', 'b', 'c', 10, 20, 30]
tuple = ('a', 'b', 'c', 40, 50, 60)
dict = {'a', 'b', 'c', 70, 80, 90}


def jekafunc():
    print('This is list:')
    print(list)


def jekafunc_2():
    print('This is tuple:')
    print(tuple)


def jekafunc_3():
    print('This is dict:')
    print(dict)


while True:
    if main_number == 1:
        print(jekafunc())
    elif main_number == 2:
        print(jekafunc_2())
    elif main_number == 3:
        print(jekafunc_3())
    else:
        print('Erorr - Please number 1-3')