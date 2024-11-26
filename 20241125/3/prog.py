class Vowel:
    __slots__ = ('a', 'e', 'i', 'o', 'u', 'y', '_values')
    
    def __init__(self, **kwargs):
        object.__setattr__(self, '_values', {letter: None for letter in self.__slots__ if letter != '_values'})
        
        for key, value in kwargs.items():
            if key in self._values:
                self._values[key] = value
            else:
                raise AttributeError(f"Invalid slot: {key}")
    
    def __getattr__(self, name):
        if name == '_values':
            raise AttributeError(f"'Vowel' object has no attribute '{name}'")
        if name in self._values:
            if self._values[name] is not None:
                return self._values[name]
            raise AttributeError(f"Slot '{name}' is uninitialized.")
        raise AttributeError(f"'Vowel' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        if name == '_values':
            raise AttributeError(f"Cannot modify '_values'")
        if name in self._values:
            self._values[name] = value
        elif name in ('answer', 'full'):
            raise AttributeError(f"Cannot modify '{name}'")
        else:
            super().__setattr__(name, value)
    
    @property
    def answer(self):
        return 42
    
    @property
    def full(self):
        return all(value is not None for value in self._values.values())
    
    def __str__(self):
        return ', '.join(f"{k}: {v}" for k, v in sorted(self._values.items()) if v is not None)


import sys
exec(sys.stdin.read())
