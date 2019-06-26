from decorators import register


@register(name="module_two")
def print_me(text):
    print("You are in module two!")
    print(text)
