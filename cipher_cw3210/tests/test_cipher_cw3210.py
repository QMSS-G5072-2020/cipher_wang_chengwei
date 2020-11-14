from cipher_cw3210.cipher_cw3210 import cipher

def test_cipher_symbols():
    example = 'Yellow!'
    shift = 1
    expected = 'Zfmmpx!'
    actual = cipher(example, shift, encrypt=True)
    assert actual == expected

test_cipher_symbols()