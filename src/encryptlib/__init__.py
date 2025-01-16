"""
ENcrypt: A Matrix-based Encryption Library

A secure and efficient encryption library using matrix operations and periodic decimal expansions,
developed as part of the TUBITAK 2204-a project.
"""

from .core import ENcrypt
from .exceptions import EncryptionError, InvalidKeyError, MessageFormatError

# List of required packages from your pyproject.toml
required_packages = [
    "numpy",
    "mpmath",
]



__version__ = "1.0.0"
__author__ = "Burak Güngör"
__email__ = "burak.gungor@enka.k12.tr"

__all__ = [
    "ENcrypt",
    "EncryptionError",
    "InvalidKeyError",
    "MessageFormatError",
]

