"""
ENcrypt: A Encryption Library

This module implements a custom encryption algorithm based on matrix operations
and periodic decimal expansions. It's designed for educational purposes as part
of the TUBITAK 2204-a project.

The encryption process uses a key derived from numbers ending in 9 to generate
a 2x2 matrix for encryption/decryption operations.

Example:
     >>> encryptor = ENcrypt(59)
     >>> encrypted = encryptor.encrypt("Hello World")
     >>> decrypted = encryptor.decrypt(encrypted)
     >>> assert "hello world" == decrypted.lower()
"""

import logging
from typing import Dict, Union, Optional

import numpy as np
from mpmath import mpf, workdps
from numpy.typing import NDArray

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Type aliases
Matrix = NDArray[np.int_]
FloatMatrix = NDArray[np.float64]

# Constants
ENCRYPT_ACCURACY = 1000  # Decimal precision for calculations
DEFAULT_ALPHABET = "abcçdefgğhiıjklmnoöprsştuüvyz "
REQUIRED_SUFFIX = "9"
PERIOD_MARKER = "89"


class EncryptionError(Exception):
    """Base exception class for encryption-related errors."""
    pass


class InvalidKeyError(EncryptionError):
    """Raised when the encryption key is invalid."""
    pass


class MessageFormatError(EncryptionError):
    """Raised when the message format is invalid."""
    pass



class ENcrypt:
    """
    A class implementing matrix-based encryption and decryption operations.

    Attributes:
        alphabet (str): The character set used for encryption/decryption.
        key (int): The encryption key derived from the input value.
        value (int): The original input value.
        approx (mpf): High-precision approximation of 1/value.
    """

    def __init__(self, value: int, alphabet: Optional[str] = None):
        """
        Initialize the encryption system with a given value and optional alphabet.

        Args:
            value: An integer ending with 9.
            alphabet: Optional custom alphabet. Defaults to Turkish alphabet with space.

        Raises:
            InvalidKeyError: If the value doesn't meet requirements.
            ValueError: If the alphabet contains duplicate characters.
        """
        self.alphabet = alphabet or DEFAULT_ALPHABET

        # Validate alphabet
        if len(set(self.alphabet)) != len(self.alphabet):
            raise ValueError("Alphabet contains duplicate characters")

        # Validate value
        if not isinstance(value, int):
            raise InvalidKeyError("Value must be an integer")
        if not str(value).endswith(REQUIRED_SUFFIX):
            raise InvalidKeyError("Value must end with '9'")

        with workdps(ENCRYPT_ACCURACY):
            self.value = value
            self.key = int(str(value)[:-1])
            self.approx = mpf(1) / mpf(value)

        logger.debug(f"Initialized Encrypt with value={value}, key={self.key}")

    @property
    def key_mat(self) -> Matrix:
        """
        Generate the encryption key matrix from the decimal expansion.

        Returns:
            A 2x2 numpy array representing the key matrix.

        Raises:
            EncryptionError: If unable to extract required digits.
        """
        with workdps(ENCRYPT_ACCURACY):
            decimal_str = str(self.approx)[2:]
            period = decimal_str.find(PERIOD_MARKER)

            if period < 2:
                raise EncryptionError("Unable to extract key matrix digits")

            try:
                a, b = decimal_str[period - 2], decimal_str[period - 1]
                c, d = decimal_str[period + 3], decimal_str[period + 4]
                matrix = np.array([[int(a), int(b)], [int(c), int(d)]], dtype=int)

                # Verify matrix is invertible
                if np.linalg.det(matrix) == 0:
                    raise EncryptionError("Generated key matrix is not invertible")

                return matrix

            except (IndexError, ValueError) as e:
                raise EncryptionError(f"Failed to generate key matrix: {str(e)}")

    @property
    def period(self) -> int:
        """Calculate the basic period in the decimal expansion."""
        with workdps(ENCRYPT_ACCURACY):
            return str(self.approx)[2:].find(PERIOD_MARKER)

    @property
    def true_period(self) -> int:
        """Calculate the true period used in encryption."""
        return (self.period * 2) + 2

    def encrypt(self, message: str) -> Matrix:
        """
        Encrypt a message using matrix multiplication.

        Args:
            message: The message to encrypt.

        Returns:
            An encrypted matrix.

        Raises:
            MessageFormatError: If message contains invalid characters.
        """
        logger.info(f"Encrypting message of length {len(message)}")

        # Validate message
        if not message:
            raise MessageFormatError("Message cannot be empty")

        invalid_chars = set(message.lower()) - set(self.alphabet)
        if invalid_chars:
            raise MessageFormatError(
                f"Message contains invalid characters: {invalid_chars}"
            )

        # Prepare message
        message = message.lower()
        if len(message) % 2:
            message += " "
            logger.debug("Padded message with space to ensure even length")

        # Convert to numeric values
        try:
            numerized_message = [self.alphabet.index(c) for c in message]
        except ValueError as e:
            raise MessageFormatError(f"Failed to convert message: {str(e)}")

        # Create message matrix
        mid = len(numerized_message) // 2
        period_offset = self.true_period % len(self.alphabet)

        vectorized_message = np.array([
            [(i + period_offset) for i in numerized_message[:mid]],
            [(i + period_offset) for i in numerized_message[mid:]]
        ])

        logger.debug(f"Key matrix:\n{self.key_mat}")
        logger.debug(f"Message matrix:\n{vectorized_message}")

        return np.matmul(self.key_mat, vectorized_message)

    def decrypt(self, mat: Union[Matrix, FloatMatrix]) -> str:
        """
        Decrypt an encrypted matrix back to text.

        Args:
            mat: The encrypted matrix to decrypt.

        Returns:
            The decrypted message.

        Raises:
            EncryptionError: If decryption fails.
        """
        logger.info("Attempting decryption")

        try:
            inverted_key = np.linalg.inv(self.key_mat)
            decrypted_matrix = np.matmul(inverted_key, mat)

            # Round to handle floating point imprecision
            decrypted_matrix = np.round(decrypted_matrix).astype(int)

            period_offset = self.true_period % len(self.alphabet)
            flattened = decrypted_matrix.flatten()

            # Convert numbers back to characters
            decrypted = "".join([
                self.alphabet[int((c - period_offset) % len(self.alphabet))]
                for c in flattened
            ])

            # Remove padding if present
            decrypted = decrypted.rstrip()

            logger.debug(f"Successfully decrypted message: {decrypted}")
            return decrypted

        except Exception as e:
            raise EncryptionError(f"Decryption failed: {str(e)}")


def main():
    """Demo function showcasing basic usage."""
    test_message = "PROJEYE BAŞLADIK"
    key = 59

    try:
        encryptor = ENcrypt(key)

        encrypted = encryptor.encrypt(test_message)
        print(f"Encrypted matrix:\n{encrypted}")

        decrypted = encryptor.decrypt(encrypted)
        print(f"Decrypted message: {decrypted}")

        # Verify
        assert decrypted.upper() == test_message
        print("Verification successful!")

    except Exception as e:
        logger.error(f"Demo failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()