class Num:
    def __init__(self, default=0):
        self.default = default
        self.name = "_value"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if hasattr(value, 'real') and hasattr(value, '__len__'):
            setattr(instance, self.name, value.real)
        elif hasattr(value, 'real'):
            setattr(instance, self.name, value.real)
        elif hasattr(value, '__len__'):
            setattr(instance, self.name, len(value))

    def __delete__(self, instance):
        setattr(instance, self.name, self.default)

import sys
exec(sys.stdin.read())
