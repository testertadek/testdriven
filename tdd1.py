import unittest

import mojprogram

class TestTDD1(unittest.TestCase):

    def test_zwroc_100(self):
        wynik = mojprogram.zwroc_100()
        self.assertEquals(wynik, 100)

    def test_inna_metoda(self):
        data = "Tadek"
        wynik = mojprogram.return_parametr(data)
        self.assertEqual(wynik, "Tadek")

if __name__ == '__main__':
    unittest.main()
