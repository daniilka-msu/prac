def objcount(cls):
    cls.counter = 0
    original_init = getattr(cls, '__init__', lambda self: None)
    def new_init(self, *args, **kwargs):
        cls.counter += 1
        original_init(self, *args, **kwargs)
    cls.__init__ = new_init
    original_del = getattr(cls, '__del__', lambda self: None)
    def new_del(self):
        cls.counter -= 1
        original_del(self)
    cls.__del__ = new_del
    return cls

import sys
exec(sys.stdin.read())
