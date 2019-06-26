import unittest
from decorators import register
from registry import GlobalRegistry


class TestDecorators(unittest.TestCase):

    def test_register(self):
        @register(name="test")
        def test_func():
            pass

        test_func()
        self.assertDictEqual(GlobalRegistry.list(), {"test": test_func})

if __name__ == '__main__':
    unittest.main()