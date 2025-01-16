# 89crypt | (ENcrypt)

> A secure and efficient matrix-based encryption library for specific use cases developed for TUBITAK 2204-a project.

## Features

- Matrix-based encryption using periodic decimal expansions
- Support for custom alphabets and character sets
- High-precision numerical operations
- Comprehensive error handling
- Type-safe implementation with full type hints
- Extensive documentation and examples

## Installation

```bash
pip install encryptlib
```

For development installation with documentation tools:

```bash
pip install "encryptlib[dev,docs]"
```

## Quick Start

```python
from encryptlib import ENcrypt

# Create an encryptor with a key
encryptor = ENcrypt(59)

# Encrypt a message
encrypted = encryptor.encrypt("Hello World")
print(f"Encrypted matrix:\n{encrypted}")

# Decrypt the message
decrypted = encryptor.decrypt(encrypted)
print(f"Decrypted message: {decrypted}")
```

## Documentation

Full documentation is available at [Read the Docs](https://encryptlib.readthedocs.io/).

## Development

1. Clone the repository:
   ```bash
   git clone https://github.com/TheBruh141/89crypt.git
   cd 89crypt
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev,docs]"
   ```

3. Run tests:
   ```bash
   pytest
   ```

4. Build documentation:
   ```bash
   cd docs
   make html
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3 - see the [LICENSE](LICENSE) file for details.

## Author

- Burak Güngör (burak.gungor@enka.k12.tr)