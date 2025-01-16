Examples
========

This page provides various examples of using ENcrypt in different scenarios.

Basic Usage
----------

Simple Message Encryption
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from encryptlib import ENcrypt

    # Create an encryptor
    encryptor = ENcrypt(59)

    # Basic encryption
    message = "HELLO WORLD"
    encrypted = encryptor.encrypt(message)
    decrypted = encryptor.decrypt(encrypted)

    print(f"Original: {message}")
    print(f"Encrypted:\n{encrypted}")
    print(f"Decrypted: {decrypted}")

Working with Custom Alphabets
---------------------------

Using a Different Character Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Define a custom alphabet (e.g., for English)
    english_alphabet = "abcdefghijklmnopqrstuvwxyz "

    # Create encryptor with custom alphabet
    encryptor = ENcrypt(59, alphabet=english_alphabet)

    message = "PYTHON ROCKS"
    encrypted = encryptor.encrypt(message)
    decrypted = encryptor.decrypt(encrypted)

Handling Special Cases
--------------------

Messages with Odd Length
^^^^^^^^^^^^^^^^^^^^^^

ENcrypt automatically handles messages with odd length by padding:

.. code-block:: python

    encryptor = ENcrypt(59)

    # Odd-length message
    message = "HELLO"
    encrypted = encryptor.encrypt(message)
    decrypted = encryptor.decrypt(encrypted)

    print(f"Original: {message}")
    print(f"Decrypted (with padding): {decrypted}")

Error Handling
------------

Handling Invalid Keys
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from encryptlib import ENcrypt, InvalidKeyError

    try:
        # This will raise an error (key doesn't end in 9)
        encryptor = ENcrypt(58)
    except InvalidKeyError as e:
        print(f"Error: {e}")

Invalid Characters
^^^^^^^^^^^^^^^

.. code-block:: python

    from encryptlib import ENcrypt, MessageFormatError

    encryptor = ENcrypt(59)

    try:
        # This will raise an error (contains numbers)
        encrypted = encryptor.encrypt("HELLO123")
    except MessageFormatError as e:
        print(f"Error: {e}")

Advanced Usage
------------

Batch Processing
^^^^^^^^^^^^^

.. code-block:: python

    def batch_encrypt(messages: list[str], key: int) -> list[np.ndarray]:
        encryptor = ENcrypt(key)
        return [encryptor.encrypt(msg) for msg in messages]

    # Example usage
    messages = ["HELLO", "WORLD", "PYTHON"]
    encrypted_batch = batch_encrypt(messages, 59)

Matrix Manipulation
^^^^^^^^^^^^^^^^

Working directly with the key matrix:

.. code-block:: python

    encryptor = ENcrypt(59)

    # Get the key matrix
    key_matrix = encryptor.key_mat
    print("Key Matrix:")
    print(key_matrix)

    # Get matrix properties
    determinant = np.linalg.det(key_matrix)
    print(f"Determinant: {determinant}")

Integration Examples
-----------------

Using with File I/O
^^^^^^^^^^^^^^^^

.. code-block:: python

    import numpy as np
    from encryptlib import ENcrypt

    def encrypt_file(filename: str, key: int) -> None:
        # Read text from file
        with open(filename, 'r') as f:
            text = f.read()

        # Encrypt
        encryptor = ENcrypt(key)
        encrypted = encryptor.encrypt(text)

        # Save encrypted matrix
        np.save(f"{filename}.encrypted", encrypted)

    def decrypt_file(filename: str, key: int) -> str:
        # Load encrypted matrix
        encrypted = np.load(f"{filename}.encrypted")

        # Decrypt
        encryptor = ENcrypt(key)
        return encryptor.decrypt(encrypted)

Web API Integration
^^^^^^^^^^^^^^^^

Example using FastAPI:

.. code-block:: python

    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from encryptlib import ENcrypt, EncryptionError

    app = FastAPI()

    class EncryptRequest(BaseModel):
        message: str
        key: int

    @app.post("/encrypt")
    async def encrypt_message(request: EncryptRequest):
        try:
            encryptor = ENcrypt(request.key)
            encrypted = encryptor.encrypt(request.message)
            return {"encrypted": encrypted.tolist()}
        except EncryptionError as e:
            raise HTTPException(status_code=400, detail=str(e))

Best Practices
------------

1. Key Selection
^^^^^^^^^^^^^^^

- Always use keys that end in 9
- Use large enough keys for security
- Keep your keys secure and private

2. Message Preparation
^^^^^^^^^^^^^^^^^^^

- Consider message length (pad if needed)
- Validate input characters
- Handle case sensitivity appropriately

3. Error Handling
^^^^^^^^^^^^^^

- Always wrap encryption/decryption in try-except blocks
- Validate input before processing
- Handle edge cases gracefully

4. Performance
^^^^^^^^^^^^

- Reuse ENcrypt instances when encrypting multiple messages
- Consider batch processing for large datasets
- Monitor matrix operations performance

Security Considerations
--------------------

While ENcrypt provides a unique encryption approach, keep in mind:

- Key selection is crucial for security
- The library is primarily for educational purposes
- Consider additional security measures for production use
- Keep encryption keys secure
- Understand the mathematical principles behind the encryption

These examples demonstrate the versatility and capabilities of ENcrypt. For more specific use cases or advanced implementations, please consult the API reference or open an issue on GitHub.