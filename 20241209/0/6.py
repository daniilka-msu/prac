class AnnotatedField:
    a: type

    def __init__(self, val):
        if not isinstance(val, self.__annotations__['a']):
            raise TypeError(f"Значение должно быть типа {self.__annotations__['a']}, получено {type(val)}")
        self.a = val

class MyClass(AnnotatedField):
    a: int

try:
    user_input = int(input("Введите целое число: "))
    obj = MyClass(user_input)
    print(f"Создан объект с значением a: {obj.a}")
except ValueError:
    print("Ошибка: введено не целое число.")
except TypeError as e:
    print(e)

