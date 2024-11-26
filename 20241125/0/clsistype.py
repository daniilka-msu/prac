class IsType:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, fun):
        def new_fun(*args):
            if all(isinstance(arg, self.typ) for arg in args):
                return fun(*args)
            raise TypeError(f'Not all {self.typ}')

        return new_fun


@IsType(int)
def int_fun(*args):
    return sum(args)


print(int_fun())


