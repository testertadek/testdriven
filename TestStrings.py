import unittest
import StringFunction

class Test():

    def test_capitalize(self):
        #user capitalize() function
        result = StringFunction.capitalize("zmien na duze")
        self.assertEqual(result, "Zmien na duze")

    def test_lower(self):
        #use lower() function
        result = StringFunction.lower("Zmien na MALE")
        self.assertEqual(result, "zmien na male")

    def test_occurance_in_String(self):
        #use count() method
        result = StringFunction.count_occurence("Ala ma kota", "a")
        self,assertEqual(result, 2)

    def test_is_lower(self):
        #use is_lower() method
        result = StringFunction.islower("ala ma kota")
        self.assertEqual(result, True)

    def test_change_as_title(self):
        #use title() method
        result = StringFunction.change_to_title("ala ma kota")
        self.assertEqual(result, "Ala Ma Kota")

if __name__ == '__main__':
    unittest.main()
