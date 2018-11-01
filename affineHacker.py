import affineCipher, detectEnglish, cryptoMath

SILENT_MODE = False

def main():
    myMessage = """+e!U1'6OJ^@!Y1O"Z!Z^E^@T^!J1!P^!UK""^Z!r,J^""rh^,J!rc!rJ!U1O"Z!Z^U^rT^!K!mO'K,!r,J1!P^"r^Tr,h!JmKJ!rJ!YKE!mO'K,f+!ae"K,!dO@r,h"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')

def hackAffine(message):
    print('Hacking...')

    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried key %s... (%s)' % (key, decryptedText[:40]))
        
        if detectEnglish.isEnglish(decryptedText):
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])

            response = input('>')
            if response.strip().upper().startswith('D'):
                return decryptedText
    
    return None

if __name__ == '__main__':
    main()
