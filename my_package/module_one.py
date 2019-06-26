from decorators import register


@register(name="module_one")
def print_me(text):
    print("You are in module one!")
    print(text)
