import pyperclip

def cipher(mode, message, key):

    # Cipher's Symbol Set
    SYMBOL_SET = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
    SYMBOL_SET_SIZE = len(SYMBOL_SET)

    result = ''
    for symbol in message:
        if symbol not in SYMBOL_SET:
            raise ValueError("Symbol encountered that is not in symbol set!")

        idx = SYMBOL_SET.find(symbol)
        if mode == 'encrypt':
            idx += key
        elif mode == 'decrypt':
            idx -= key
        else:
            raise ValueError('Mode not supported!')

        if idx >= SYMBOL_SET_SIZE:
            idx -= SYMBOL_SET_SIZE
        elif idx < 0:
            idx += SYMBOL_SET_SIZE

        result += SYMBOL_SET[idx]

    return result

print("Caesar Cipher")

print("Input method (encrypt or decrypt):")
mode = input()

print("Input message: ")
message = input()

print("Input key 0 - 25: ")
key = int(input())

result = cipher(mode, message, key)
print(result)
