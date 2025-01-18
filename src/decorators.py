from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar

P = ParamSpec('P')  # Для аргументов
R = TypeVar('R')  # Для возвращаемых значений


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, None]]:
    """Записывает в файл или в консоль статус выполнения функции (успешно или ошибка)"""

    def my_dec(function: Callable[P, R]) -> Callable[P, None]:
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> None:
            try:
                function(*args, **kwargs)
            except Exception as e:
                message = f'{function.__name__} error: {e}. Inputs: {args, kwargs}'
            else:
                message = f'{function.__name__} ok'
            finally:
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(message)
                else:
                    print(message)

        return wrapper

    return my_dec
