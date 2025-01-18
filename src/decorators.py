from typing import TypeVar, ParamSpec, Optional, Callable

P = ParamSpec('P')  # Для аргументов
R = TypeVar('R')  # Для возвращаемых значений


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, None]]:
    """Записывает в файл или в консоль статус выполнения функции (успешно или ошибка)"""

    def my_dec(function: Callable[P, R]) -> Callable[P, None]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> None:
            try:
                function(*args, **kwargs)
            except Exception as e:
                message = f'{function} error: {e}. Inputs: {args, kwargs}\n'
            else:
                message = f'{function} ok\n'
            finally:
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(message)
                else:
                    print(message)

        return wrapper

    return my_dec
