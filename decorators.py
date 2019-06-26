from registry import GlobalRegistry


def register(name):
    def decorator_register(func):
        GlobalRegistry.register(name, func)
        return func

    return decorator_register
