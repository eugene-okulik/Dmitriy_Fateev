def repeat_me(func):
    def wrapper(text, count=1):

        result = [func(text) for _ in range(count)]
        return result

    return wrapper


@repeat_me
def example(text):
    print(text)
    return text


example("print me", count=2)
