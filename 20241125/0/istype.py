def istype(typ):
    def dec(fun):
        def new_fun(*args):
            if all(isinstance(arg, typ) for arg in args):
                return fun(*args)
            raise TypeError
        return new_fun
    return dec


@istype(str)
def add(x, y):
    return x + y


print(add('a', 's'))
try:
    print(add(1, 3))
except TypeError:
    print('TypeError')
