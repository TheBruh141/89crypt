"""Utility functions for the encryptlib package."""

import numpy as np
from numpy.typing import NDArray
from typing import Dict

def matrix_to_numbers(matrix: NDArray, alphabet: str) -> NDArray[np.int_]:
    """
    Convert a matrix of characters to a matrix of numbers based on the alphabet.

    Args:
        matrix: The input matrix containing characters.
        alphabet: The alphabet to use for conversion.

    Returns:
        A matrix of corresponding numeric values.

    Raises:
        ValueError: If a character is not found in the alphabet.
    """
    char_to_number: Dict[str, int] = {char: idx for idx, char in enumerate(alphabet)}

    def convert(char: str) -> int:
        if char not in char_to_number:
            raise ValueError(f"Character '{char}' not found in alphabet")
        return char_to_number[char]

    return np.vectorize(convert)(matrix)

def validate_alphabet(alphabet: str) -> None:
    """
    Validate the provided alphabet.

    Args:
        alphabet: The alphabet to validate.

    Raises:
        ValueError: If the alphabet contains duplicate characters.
    """
    if len(set(alphabet)) != len(alphabet):
        raise ValueError("Alphabet contains duplicate characters")