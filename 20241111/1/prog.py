class Omnibus:
    _attributes = {}

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        if name not in Omnibus._attributes:
            Omnibus._attributes[name] = set()
        if self not in Omnibus._attributes[name]:
            Omnibus._attributes[name].add(self)

    def __getattr__(self, name):
        if name.startswith("_") or name not in Omnibus._attributes:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        return len(Omnibus._attributes[name])

    def __delattr__(self, name):
        if name.startswith("_") or name not in Omnibus._attributes:
            return
        if self in Omnibus._attributes[name]:
            Omnibus._attributes[name].remove(self)
        if not Omnibus._attributes[name]:
            del Omnibus._attributes[name]


import sys

exec(sys.stdin.read())
