import unittest

import hello_word

class TestTDD2(unittest.TestCase):

    def test_print_hello(self):
        result = hello_word.print_hello()
        self.assertEquals(result, "hello word")

if __name__ == '__main__':
    unittest.main()
