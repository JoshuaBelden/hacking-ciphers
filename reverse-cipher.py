def EncodeDecode(message):
    result = ''
    
    i = len(message) - 1
    while i >= 0:
        result += message[i]
        i -= 1

    return result

print('Type a message: ')
message = input()

encoded = EncodeDecode(message)
print("Encoded message: " + encoded)

decoded = EncodeDecode(encoded)
print("Decoded message: " + decoded)
