"""Exception classes for the encryptlib package."""

class EncryptionError(Exception):
    """Base exception class for encryption-related errors."""
    pass

class InvalidKeyError(EncryptionError):
    """Raised when the encryption key is invalid."""
    pass

class MessageFormatError(EncryptionError):
    """Raised when the message format is invalid."""
    pass
