import unittest

from ENcrypt import ENcrypt


class TestENcrypt(unittest.TestCase):

    def test_initialization(self):
        """Test that the ENcrypt object initializes correctly with value 10"""
        encrypt_obj = ENcrypt()
        self.assertEqual(encrypt_obj.value, 10)

    def test_str_method(self):
        """Test that the __str__ method returns the correct string representation"""
        encrypt_obj = ENcrypt()
        self.assertEqual(str(encrypt_obj), "10")


if __name__ == '__main__':
    unittest.main()
