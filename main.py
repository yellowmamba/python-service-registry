from my_package import *
from registry import GlobalRegistry


if __name__ == "__main__":
	print_me = GlobalRegistry.dispatch("module_one")
	print_me("this is some text")

	print_me = GlobalRegistry.dispatch("module_two")
	print_me("this is some other text")