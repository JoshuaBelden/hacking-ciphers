# Cipher's Symbol Set
SYMBOL_SET = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
SYMBOL_SET_SIZE = len(SYMBOL_SET)

def cipher(mode, message, key):

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

message = 'k!",8",8x8,.)}+8,}{+}-8&},,x }'

for key in range(SYMBOL_SET_SIZE):
    print('Key: %s - Message: %s' % (key, cipher('decrypt', message, key)))

