class C:
    @property
    def age(self):
        if self._age == 42:
            print("secret value!")
            return -1
        return self._age

    @age.setter
    def age(self, val):
        if val <= 128:
            self._age = val
        else:
            raise ValueError("age too old!")


c = C()
c.age = 12
print(c.age)
c.age = 128
print(c.age)
try:
    c.age = 129
except ValueError as e:
    print("too old!")
