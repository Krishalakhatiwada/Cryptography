# SHA-512 Hashing Algorithm Implementation

SHA-512 is a cryptographic hash function that takes an input message and produces a fixed-length (512-bit) hash value. This implementation consists of several functions that together implement the SHA-512 algorithm.

## Code Documentation

### `right_rotate(x, n)`

This function takes an input `x` and rotates its bits to the right by `n` positions.

### `a_summation(a)`

This function implements one of the SHA-512 message schedule functions. It performs bitwise operations on the input `a` by right-rotating it by 28, 34, and 39 bits and then applying XOR operations.

### `e_summation(e)`

Similar to `a_summation(a)`, this function implements another SHA-512 message schedule function. It right-rotates the input `e` by 14, 18, and 41 bits and applies XOR operations.

### `ch(e, f, g)`

This function implements the "Ch" operation used in the SHA-512 algorithm. It performs a bitwise AND operation between `e` and `f`, and then applies a bitwise NOT operation to `e` and performs a bitwise AND operation with `g`. Finally, it XORs the results.

### `maj(a, b, c)`

This function implements the "Maj" operation used in the SHA-512 algorithm. It performs a bitwise AND operation between `a` and `b`, another between `a` and `c`, and finally XORs the results.

### `sigma_1(x)`

This function implements the "Sigma1" operation used in the SHA-512 algorithm. It right-rotates the input `x` by 19 and 61 bits and performs a right shift by 6 bits, followed by XOR operations.

### `sigma_0(x)`

Similar to `sigma_1(x)`, this function implements the "Sigma0" operation. It right-rotates the input `x` by 1 and 8 bits and performs a right shift by 7 bits, followed by XOR operations.

### `padding_msg(message)`

This function adds padding to the input message to ensure its length is a multiple of 128 bytes (1024 bits), which is a requirement of the SHA-512 algorithm. It appends a single '1' bit, followed by '0' bits to the message. Then, it appends the original message length as a 128-bit big-endian integer.

### `divide_into_blocks(padded_msg)`

This function divides the padded message into 128-byte blocks.

### `wt(message)`

This function is intended to populate the message schedule array `w` by processing the message block. However, it appears to be incomplete in the provided code.

### Constants

- `K`: An array of constants used in the SHA-512 algorithm.
- `H`: An array of initial hash values.

### `sha_512(message)`

This function is the main SHA-512 hashing algorithm. It takes an input message, processes it block by block, updates the internal state variables, and finally produces the hash value in the `H` array.

### Main Execution

The main execution block reads an input message from the user, encodes it, applies padding, divides it into blocks, and processes each block using the `sha_512` function. Finally, it prints the resulting hash value.

## Workflow

1. User provides an input message.
2. The message is encoded in UTF-8 and padded.
3. The padded message is divided into 128-byte blocks.
4. Each block is processed using the `sha_512` function, which updates the hash values in the `H` array.
5. After processing all blocks, the final hash value is printed.

This code provides a basic implementation of the SHA-512 hashing algorithm, but it seems to be incomplete and contains some issues. You may need to complete the `wt` function and ensure that the message schedule is correctly generated for the algorithm to work properly. Additionally, you might want to consider error handling and testing for robustness.
