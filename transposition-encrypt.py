def main():
    message = "Common sense is not so common!"
    key = 8
    cipherText = encrypt(key, message)
    print(cipherText + '|')

def encrypt(key, message):
    cipherText = [''] * key

    for cipher_idx in range(key):
        message_idx = cipher_idx
        while message_idx < len(message):
            cipherText[cipher_idx] += message[message_idx]
            message_idx += key
        
    return ''.join(cipherText)

if __name__ == '__main__':
    main()