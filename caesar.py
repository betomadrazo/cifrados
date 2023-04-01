BASE = 65

def caesar_cipher(message, key):
    key_as_num = convert_char_to_number(key)
    print(key_as_num)

def convert_char_to_number(key):
    return ord(key) - BASE

def watch(number, mod):
    return number % mod
