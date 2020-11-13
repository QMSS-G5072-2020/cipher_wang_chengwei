def cipher(text, shift, encrypt=True):
    """
    Encrypt or decrypt strings/documents by changing letters to
    letters before or after them.

    Parameters
    ----------
    text: string
        The original text you want to encrypt or decrypt.
    shift: numeric
        how far the encrypted (or decrypted) letter from the original letter in the text
    encrypt: boolean
        if true, then the function will transfer your (presumably) readable text into
        encrypted ones. If false, if will try to decrypt your text by the "key" (shift) you offered.

    Returns
    -------
    string
        The encrypted / decrypted string.

    Examples
    --------
    >>> cipher(text="text", shift=1, encrypt=True)
    'ufyu'
    >>> cipher(text="ufyu", shift=1, encrypt=False) # returns "text"
    'text'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

