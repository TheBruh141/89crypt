"""Tests for the core encryption functionality."""

"""
Note for pycharm users:
    please check the output of the tests carefully. For some reason even tho we are expecting errors to arise
    the ide does not detect them and causing false positives (or negatives in our case). 

"""

import pytest
import numpy as np

from src.encryptlib import ENcrypt, InvalidKeyError, MessageFormatError


def test_encryption_decryption():
    """Test basic encryption and decryption functionality."""
    encryptor = ENcrypt(59)
    message = "HELLO WORLD"

    encrypted = encryptor.encrypt(message)
    decrypted = encryptor.decrypt(encrypted)

    assert decrypted.upper() == message

def test_invalid_key():
    """Test that invalid keys raise appropriate errors."""
    with pytest.raises(InvalidKeyError) as e:
        ENcrypt(58)  # Number not ending in 9

def test_empty_message():
    """Test handling of empty messages."""
    encryptor = ENcrypt(59)
    with pytest.raises(MessageFormatError) :
        encryptor.encrypt("")

def test_invalid_characters():
    """Test handling of invalid characters in messages."""
    encryptor = ENcrypt(59)
    with pytest.raises(MessageFormatError):
        encryptor.encrypt("Hello123!")  # Numbers and punctuation not in alphabet

def test_custom_alphabet():
    """Test encryption with custom alphabet."""
    custom_alphabet = "abcdefghijklmnopqrstuvwxyz "
    encryptor = ENcrypt(59, alphabet=custom_alphabet)
    message = "HELLO WORLD"

    encrypted = encryptor.encrypt(message)
    decrypted = encryptor.decrypt(encrypted)

    assert decrypted.upper() == message

def test_matrix_invertibility():
    """Test that generated key matrices are invertible."""
    encryptor = ENcrypt(59)
    matrix = encryptor.key_mat
    det = np.linalg.det(matrix)
    assert det != 0