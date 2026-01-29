from functools import wraps
from typing import Any, Callable, Optional, Union


def log(filename: Optional[str] = None) -> Callable:
    """Функция-декоратор"""

    def decorator(func: Any) -> Any:
        """Декоратор для оборачивания функции функцией-оберткой"""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Функция-обертка"""
            try:
                message1 = f"Функция '{func.__name__}' начала работу с входными параметрами: {args}, {kwargs}"
                message2 = "Результат работы:"
                message3 = f"Функция '{func.__name__}' окончила работу успешно"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message1 + "\n")
                else:
                    print(message1)
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as f:
                        f.write(message2 + str(result) + "\n")
                        f.write(message3 + "\n")
                else:
                    print(message2, result)
                    print(message3)
                return result
            except Exception as e:
                message4 = f"Произошла ошибка {e}"
                message5 = f"Функция '{func.__name__}' окончила работу"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message4 + "\n")
                        f.write(message5 + "\n")
                else:
                    print(message4)
                    print(message5)
                raise

        return wrapper

    return decorator


@log()
def summa(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y
