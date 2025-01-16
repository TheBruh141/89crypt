import unittest
import numpy as np
from mpmath import mpf
from ENcrypt import (
    matrix_to_numbers,
    ENcrypt,
)


class TestMatrixToNumbers(unittest.TestCase):
    def test_matrix_to_numbers_basic(self):
        matrix = np.array([["a", "b"], ["c", " "]])
        alphabet = "abcçdefgğhiıjklmnoöprsştuüvyz "
        expected = np.array([[0, 1], [2, 29]])
        result = matrix_to_numbers(matrix, alphabet)
        np.testing.assert_array_equal(result, expected)


class TestENcrypt(unittest.TestCase):
    def test_init_valid_value(self):
        encryptor = ENcrypt(123456789)
        self.assertEqual(encryptor.value, 123456789)
        self.assertEqual(encryptor.key, 12345678)
        self.assertTrue(isinstance(encryptor.approx, mpf))

    def test_init_invalid_value(self):
        with self.assertRaises(ValueError):
            ENcrypt(12345678)  # Does not end with '9'

    def test_key_mat(self):
        encryptor = ENcrypt(123456789)
        key_mat = encryptor.key_mat
        self.assertEqual(key_mat.shape, (2, 2))
        self.assertTrue(np.issubdtype(key_mat.dtype, np.integer))

    def test_encrypt_decrypt(self):
        encryptor = ENcrypt(59)
        message = "merhaba dunya"
        encrypted = encryptor.encrypt(message)
        decrypted = encryptor.decrypt(encrypted)
        self.assertEqual(message, decrypted.strip())

    def test_encrypt_message_length(self):
        encryptor = ENcrypt(123456789)
        message = "oddlength"
        encrypted = encryptor.encrypt(message)
        self.assertEqual(encrypted.shape[1], (len(message) + 1) // 2)

    def test_period_properties(self):
        encryptor = ENcrypt(123456789)
        self.assertGreater(encryptor.period, 0)
        self.assertEqual(encryptor.true_period, (encryptor.period * 2) + 2)


if __name__ == "__main__":
    unittest.main()
