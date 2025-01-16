.. title:: Algorithm

Algorithm
=========

In this part of the documentation, we will try to explain what is going on under the hood of this library.

1. Mathematical Foundation
---------------------------

1.1 The Special Property of 1/89
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method is based on an interesting mathematical property of the number 89, which appears in its own decimal expansion when written as :math:`\frac{1}{89}`:

.. math::
    \frac{1}{89} = 0.011235955056179775280898876404494382022471910112359...

Key properties:
- The decimal expansion has a period of 44 digits
- The number "89" appears symmetrically in the middle of this period
- This creates a natural cryptographic seed

1.2 Generalization to :math:`\frac{1}{n9}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The method extends this property to numbers of the form :math:`\frac{1}{n9}`, where :math:`n` is a positive integer. Many such numbers exhibit similar symmetric properties with "89" appearing in their decimal expansions.

.. math::
    \frac{1}{49} = 0.\underbrace{02040816326530612244}_{\text{20 characters here}}\underbrace{\textbf{89}}_{+2}\underbrace{79591836734693877551}_{\text{the next 20}}...

- Period: 42 digits
- Symmetric pattern around "89"

2. Cryptographic Algorithm
--------------------------

### 2.1 Key Generation
For a given :math:`n`, three cryptographic keys are generated:
1. Primary key :math:`n` (determines which :math:`\frac{1}{n9}` fraction to use)
2. Matrix key :math:`K` (2×2 matrix derived from decimal digits)
3. Caesar shift key :math:`p` (derived from period length)

### 2.2 Matrix Formation
The key matrix :math:`K` is formed using four digits from the decimal expansion:

.. math::
    K = \begin{bmatrix} u & v \\ x & y \end{bmatrix}

where :math:`uv` and :math:`xy` are two-digit numbers selected from positions around "89" in the expansion.

Requirements for :math:`K`:
- :math:`\text{det}(K) \neq 0` (matrix must be invertible)
- :math:`\text{det}(K) = u \cdot y - v \cdot x`

### 2.3 Caesar Shift Calculation
For period :math:`d` of :math:`\frac{1}{n9}`:

.. math::
    p = d \mod 10

3. Encryption Process
---------------------

### 3.1 Message Preprocessing
1. Convert message to numerical values using alphabet mapping
2. Apply Caesar shift of :math:`p` positions
3. Form matrix :math:`M` of dimensions :math:`2 \times \lceil \frac{m}{2} \rceil` where :math:`m` is message length

### 3.2 Matrix Encryption
The encryption process uses Hill cipher methodology:

.. math::
    C = K \cdot M

where:
- :math:`C` is the encrypted matrix
- :math:`K` is the key matrix
- :math:`M` is the message matrix

4. Decryption Process
---------------------

### 4.1 Matrix Decryption
The decryption process involves:
1. Computing :math:`K^{-1}` (inverse of key matrix)
2. Computing :math:`M = K^{-1} \cdot C`
3. Applying reverse Caesar shift of :math:`-p` positions

For :math:`2 \times 2` matrix :math:`K`:

.. math::
    K^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}

5. Security Analysis
--------------------

5.1 Security Features
^^^^^^^^^^^^^^^^^^^^^

1. Multiple layers of encryption:
   - Hill cipher (matrix multiplication)
   - Caesar shift
   - Symmetric number properties
2. Three independent keys:
   - :math:`n` (primary key)
   - :math:`K` (matrix key)
   - :math:`p` (shift key)

5.2 Cryptographic Strength
^^^^^^^^^^^^^^^^^^^^^

The method combines:
- Modular arithmetic (Caesar cipher)
- Linear algebra (Hill cipher)
- Number theory (decimal expansion properties)

Making it resistant to:
- Known plaintext attacks
- Brute force attempts (due to multiple key layers)

6. Implementation Example
--------------------------

For :math:`n = 4` (using :math:`\frac{1}{49}`):

Step 1: **Decimal Expansion**

We begin by considering the decimal expansion of :math:`\frac{1}{49}`:

.. math::
    \frac{1}{49} = 0.\underbrace{02040816326530612244}_{\text{20 characters here}}\underbrace{\textbf{89}}_{+2}\underbrace{79591836734693877551}_{\text{the next 20}}...

Step 2: **Key Generation**

- Primary key :math:`n = 4`
- Matrix key :math:`K` is derived from the decimal digits around "89". We will extract two two-digit numbers, say :math:`u = 20`, :math:`v = 40`, :math:`x = 89`, and :math:`y = 79`, from the expansion.

Thus, the key matrix :math:`K` is:

.. math::
    K = \begin{bmatrix} 20 & 40 \\ 89 & 79 \end{bmatrix}

Step 3: **Caesar Shift Calculation**

The period of the decimal expansion for :math:`\frac{1}{49}` is 42 digits. We calculate the Caesar shift key :math:`p`:

.. math::
    p = 42 \mod 10 = 2

Step 4: **Message Preprocessing**

Suppose the message is "HELLO". First, we map the letters to numerical values (e.g., H = 7, E = 5, L = 12, O = 15):

- Message: [7, 5, 12, 12, 15]
- Apply Caesar shift of 2 positions: [9, 7, 14, 14, 17] (by shifting each number by 2)

Step 5: **Matrix Formation**

Now we form the message matrix :math:`M` with dimensions :math:`2 \times \lceil \frac{5}{2} \rceil = 2 \times 3`:

.. math::
    M = \begin{bmatrix} 9 & 14 & 17 \\ 7 & 12 & 14 \end{bmatrix}

Step 6: **Matrix Encryption**

The encryption step involves matrix multiplication between the key matrix :math:`K` and the message matrix :math:`M`:

.. math::
    C = K \cdot M = \begin{bmatrix} 20 & 40 \\ 89 & 79 \end{bmatrix} \cdot \begin{bmatrix} 9 & 14 & 17 \\ 7 & 12 & 14 \end{bmatrix}

Step 7: **Decryption**

To decrypt the message, we compute the inverse of the key matrix :math:`K^{-1}`. First, we compute the determinant of :math:`K`:

.. math::
    \text{det}(K) = 20 \cdot 79 - 40 \cdot 89 = 1580 - 3560 = -1980

Now, we calculate the inverse of :math:`K`:

.. math::
    K^{-1} = \frac{1}{\text{det}(K)} \begin{bmatrix} 79 & -40 \\ -89 & 20 \end{bmatrix}
    K^{-1} = \frac{1}{-1980} \begin{bmatrix} 79 & -40 \\ -89 & 20 \end{bmatrix}

Step 8: **Final Message Recovery**

Using the inverse key matrix, we can now decrypt the encrypted matrix :math:`C` by computing :math:`M = K^{-1} \cdot C`. Finally, we reverse the Caesar shift to obtain the original message.

