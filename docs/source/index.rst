Welcome to encryptlib's documentation!
====================================
Contents
--------

.. toctree::
   :maxdepth: 2

   encryptlib
   algorithm
   examples
   tutorial

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


**encryptlib** is a Python library for secure matrix-based encryption, developed as a part of a TUBITAK 2204-a project.

Features
--------

- Matrix-based encryption using periodic decimal expansions on guaranteed values
- Customizable alphabets for different languages
- High-precision numerical operations
- Comprehensive error handling
- Type-safe implementation

Installation
------------

To install encryptlib, run this command in your terminal:

.. code-block:: console

    $ pip install encryptlib

Usage
-----

Here's a simple example:

.. code-block:: python

    from encryptlib import ENcrypt

    # Create an encryptor with a key
    encryptor = ENcrypt(59)

    # Encrypt a message
    encrypted = encryptor.encrypt("Hello World")

    # Decrypt the message
    decrypted = encryptor.decrypt(encrypted)
    assert "hello world" == decrypted.lower()

