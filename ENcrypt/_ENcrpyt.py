import numpy as np
from mpmath import mpf
from mpmath import workdps

ENCRYPT_ACCURACY = 1000


def matrix_to_numbers(matrix: np.ndarray, alphabet: str):
    """Converts a numpy matrix of characters to a matrix of numbers based on the alphabet."""

    # Create a dictionary to map each character to its corresponding index
    char_to_number = {char: idx for idx, char in enumerate(alphabet)}

    # Use the dictionary to convert each element in the matrix to a corresponding number
    num_matrix = np.vectorize(char_to_number.get)(matrix)

    return num_matrix


class ENcrypt:
    alphabet: str = "abcçdefgğhiıjklmnoöprsştuüvyz "
    key: int
    value: int
    approx: mpf

    @workdps(ENCRYPT_ACCURACY)
    def __init__(self, value: int):
        # Ensure value ends with "9"
        if str(value)[-1] != "9":
            raise ValueError("your number has to end with 9")

        self.value = value
        self.key = int(str(value)[:-1])  # Remove last character to get the key
        self.approx = mpf(1) / mpf(value)  # Set arbitrary precision approximation

    @property
    @workdps(ENCRYPT_ACCURACY)
    def key_mat(self):
        decimal_str = str(self.approx)[2:]
        period = decimal_str.find("89")
        a, b, c, d = (
            decimal_str[period - 2],
            decimal_str[period - 1],
            decimal_str[period + 3],
            decimal_str[period + 4],
        )
        # Create the key matrix from extracted values
        return np.array([[int(a), int(b)], [int(c), int(d)]], dtype=int)

    @property
    @workdps(ENCRYPT_ACCURACY)
    def period(self):
        return str(self.approx)[2:].find("89")

    @property
    @workdps(ENCRYPT_ACCURACY)
    def true_period(self):
        return (self.period * 2) + 2

    @workdps(ENCRYPT_ACCURACY)
    def encrypt(self, message: str):
        # if you are confused about why we are doing it like this look at the self.key's implementation

        print("Key Matrix:")
        print(self.key_mat)

        # Prepare the message (ensure the length is even)
        message = message if len(message) % 2 == 0 else message + " "
        print("Message prepared:", message)

        # Convert message into numeric values using the alphabet
        numerized_message = [self.alphabet.find(c) for c in message.lower()]
        mid = numerized_message.__len__() // 2
        vectorized_message = np.array(
            (
                [(i + (self.true_period % 10)) for i in numerized_message[:mid]],
                [(i + (self.true_period % 10)) for i in numerized_message[mid:]],
            )
        )

        print("Numerized Message Matrix:")
        print(vectorized_message)
        return np.matmul(self.key_mat, vectorized_message)

    @workdps(ENCRYPT_ACCURACY)
    def decrypt(self, mat: np.array) -> str:
        inverted_key = np.linalg.inv(self.key_mat)
        flattened = np.matmul(inverted_key, mat).flatten()
        s = "".join(
            [self.alphabet[int((c - self.true_period % 10) % 30)] for c in flattened]
        )
        return s


if __name__ == "__main__":
    """
    A simple way to test the library without running the whole test suite
    """
    print(ENcrypt(59).encrypt("PROJEYE BAŞLADIK"))
    print("decrpytion")

    res = ENcrypt(59).decrypt(mat=ENcrypt(59).encrypt("PROJEYE BAŞLADIK"))
    print(f"{res=}")
