def encrypt(message: str, shifts: list, alphabet: str) -> str:
    """Used to encrypt a message by shifting character indexes

    Args:
        message (str): The message to encrypt
        shifts (list): A list of integers to shift the character indexes by
        alphabet (str): The character set to use

    Raises:
        ValueError:
            If the length of the shift list is different to the length of the
            message
        ValueError:
            If the a shift value is below zero or greater than the length of
            the alphabet
        ValueError:
            If the message contains a character not found in the alphabet

    Returns:
        str: The encrypted message
    """
    if len(shifts) != len(message):
        raise ValueError
    alpha_len = len(alphabet)
    encrypted_message = ""
    for i in range(len(message)):
        if shifts[i] < 0 or shifts[i] >= alpha_len:
            raise ValueError
        # get the index of the character and shift it
        char_index = alphabet.index(message[i])
        encrypted_char_index = (char_index+shifts[i]) % alpha_len
        # get the character of the shifted index and append to message
        encrpyted_char = alphabet[encrypted_char_index]
        encrypted_message += encrpyted_char
    return encrypted_message
