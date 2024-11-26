def isint(fun):
    def new_fun(*args):
        if all(isinstance(arg, int) for arg in args):
            return fun(*args)
        raise TypeError
    return new_fun

@isint
def fun(a, b):
    return a + b

print(fun(1, 2))
