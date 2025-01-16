Tutorial
========

This tutorial will guide you through using ENcrypt for secure message encryption.

Understanding the Basics
----------------------

ENcrypt uses a unique approach to encryption based on:

1. Matrix operations
2. Periodic decimal expansions
3. Custom alphabets
4. High-precision arithmetic

The Mathematics Behind ENcrypt
---------------------------

Key Generation
^^^^^^^^^^^^

The encryption key is derived from a number ending in 9:

1. The input value must end with 9 (e.g., 59, 119, 229)
2. A high-precision division (1/value) creates a decimal expansion
3. Specific digits from this expansion form the key matrix

Matrix Operations
^^^^^^^^^^^^^^^

The encryption process involves:

1. Converting text to numbers using the alphabet
2. Creating a message matrix
3. Multiplying with the key matrix
4. Applying periodic offsets

Step-by-Step Guide
----------------

1. Installation
^^^^^^^^^^^^^

First, install ENcrypt:

.. code-block:: console

    $ pip install encryptlib

2. Basic Setup
^^^^^^^^^^^^

Import and create an encryptor:

.. code-block:: python

    from encryptlib import ENcrypt

    # Create an encryptor with key 59
    encryptor = ENcrypt(59)

3. Encrypting Messages
^^^^^^^^^^^^^^^^^^^

Simple message encryption:

.. code-block:: python

    # Prepare your message
    message = "HELLO WORLD"

    # Encrypt it
    encrypted = encryptor.encrypt(message)
    print(f"Encrypted matrix:\n{encrypted}")

4. Decrypting Messages
^^^^^^^^^^^^^^^^^^^

Decrypt the encrypted matrix:

.. code-block:: python

    # Decrypt the message
    decrypted = encryptor.decrypt(encrypted)
    print(f"Decrypted message: {decrypted}")

Advanced Features
--------------

Custom Alphabets
^^^^^^^^^^^^^

Use different character sets:

.. code-block:: python

    # Define a custom alphabet
    custom_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 "

    # Create encryptor with custom alphabet
    custom_encryptor = ENcrypt(59, alphabet=custom_alphabet)

Error Handling
^^^^^^^^^^^^

Proper error handling in your applications:

.. code-block:: python

    from encryptlib import ENcrypt, EncryptionError

    try:
        encryptor = ENcrypt(59)
        encrypted = encryptor.encrypt("Hello World")
        decrypted = encryptor.decrypt(encrypted)
    except EncryptionError as e:
        print(f"Encryption error: {e}")

Key Management
^^^^^^^^^^^^

Best practices for key selection:

.. code-block:: python

    def is_valid_key(key: int) -> bool:
        return str(key).endswith('9') and key > 0

    # Example usage
    key = 59
    if is_valid_key(key):
        encryptor = ENcrypt(key)
    else:
        print("Invalid key")

Next Steps
---------

After mastering these basics, you can:

1. Explore the :doc:`examples` page for more use cases
2. Check the :doc:`api` documentation for detailed reference
3. Learn about security considerations in :doc:`security`
4. Contribute to the project following our :doc:`contributing` guide

Tips and Tricks
-------------

1. Performance Optimization
^^^^^^^^^^^^^^^^^^^^^^^^

- Reuse encryptor instances when possible
- Consider message size and matrix operations
- Use appropriate key sizes for your needs

2. Security Considerations
^^^^^^^^^^^^^^^^^^^^^^^

- Choose appropriate key sizes
- Secure key storage
- Understand the encryption limitations

3. Debugging
^^^^^^^^^^

Enable logging for better debugging:

.. code-block:: python

    import logging
    logging.basicConfig(level=logging.DEBUG)

Common Issues
-----------

1. Invalid Keys
^^^^^^^^^^^^

- Keys must end in 9
- Keys must be positive integers

2. Character Set Issues
^^^^^^^^^^^^^^^^^^^

- Messages must use characters from the alphabet
- Case sensitivity considerations
- Handling special characters

3. Matrix Operations
^^^^^^^^^^^^^^^^^

- Understanding matrix invertibility
- Handling numerical precision
- Performance with large messages

Getting Help
----------

If you need assistance:

1. Check the documentation
2. Look through the examples
3. Open an issue on GitHub
4. Join our community discussions

Remember to consult the :doc:`api` reference for detailed information about specific functions and classes.