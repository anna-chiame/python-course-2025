from functools import wraps


class TypeDecorators:
    """
        Клас для створення декораторів, які змінюють тип результату функції.

        Методи:
            - to_int: перетворює результат функції у тип int
            - to_str: перетворює результат функції у тип str
            - to_bool: перетворює результат функції у тип bool
            - to_float: перетворює результат функції у тип float
    """

    @staticmethod
    def to_int(func):
        """
        Декоратор, що перетворює результат функції у тип integer, якщо це можливо

        :param func: функція, результат якої потрібно перетворити.
        :return wrapper : обгортка, яка повертає результат типу int.
        """
    #не губимо ім"я та docstring func
        @wraps(func)
        def wrapper(*args, **kwargs) :
            # викликаємо оригинальну func
            result = func (*args, **kwargs)
            #пробуємо перетворити
            try :
                return int(result)
            # якщо не можливо то видаємо помилку
            except  (ValueError, TypeError):
                return f"Неможливо перетворити '{result}' в тип int"
        return wrapper

    @staticmethod
    def to_str(func):
        """Декоратор, що перетворює результат функції у тип string,
           це можливо завжди і перевірки не потрібно

        :param func: функція, результат якої потрібно перетворити.
        :return wrapper : обгортка, яка повертає результат типу str.
        """
        @wraps(func)
        def wrapper(*args, **kwargs) :
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        """Декоратор, що перетворює результат функції у тип bool, якщо це можливо

        :param func: функція, результат якої потрібно перетворити.
        :return wrapper : обгортка, яка повертає результат типу bool.
        """

        @wraps(func)
        def wrapper(*args, **kwargs) :
            result = func (*args, **kwargs)
            # перевіряємо чи не є рядок чимось що є False
            new_result = result.lower().strip()
            if new_result in ("", "false", "0" ) :
                return False
            else :
                return True
        return wrapper

    @staticmethod
    def to_float(func) :
        """Декоратор, що перетворює результат функції в тип float, якщо це можливо

        :param func: функція, результат якої потрібно перетворити.
        :return wrapper : обгортка, яка повертає результат типу float.
        """
        @wraps(func)
        def wrapper(*args, **kwargs) :
            result = func(*args, **kwargs)
            try :
                return float(result)
            except (ValueError, TypeError) :
                return f"Неможливо перетворити '{result}' в тип float"
        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

@TypeDecorators.to_float
def do_anything(string: str):
    return string

# Приклади перевірки
print(do_nothing("25"))
print(do_something("True"))
print(do_something(""))
print(do_anything("4-4"))

