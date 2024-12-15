class dump(type):
    def __new__(cls, name, bases, class_dict):
        for attr_name, attr_value in class_dict.items():
            if callable(attr_value) and hasattr(attr_value, "__code__"):
                def make_wrapper(method):
                    def wrapper(self, *args, **kwargs):
                        print(f"{method.__name__}: {args}, {kwargs}")
                        return method(self, *args, **kwargs)
                    return wrapper

                class_dict[attr_name] = make_wrapper(attr_value)
        return super().__new__(cls, name, bases, class_dict)

import sys
exec(sys.stdin.read())