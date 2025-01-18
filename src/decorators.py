def log(filename=False):
    def my_dec(function):
        def wrapper(*args, **kwargs):
            try:
                function(*args, **kwargs)
            except Exception as e:
                massage = f'{function} error: {e}. Inputs: {args, kwargs}\n'
            else:
                massage = f'{function} ok\n'
            finally:
                if filename:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(massage)
                else:
                    print(massage)

        return wrapper

    return my_dec
