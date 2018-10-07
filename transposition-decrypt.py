import math

def main():
    message = 'Cenoonommstmme oo snnio. s s c'
    key = 8
    plain_text = decryptMessage(key, message)
    print(plain_text + '|')

def decryptMessage(key, message):
    ncols = math.ceil(len(message) / key)
    nrows = key
    shades = (ncols * nrows) - len(message)
    plain_text = [''] * ncols

    col = 0
    row = 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1
        if (col == ncols) or (col == ncols - 1 and row >= nrows - shades):
            col = 0
            row += 1
        
    return ''.join(plain_text)

if __name__ == '__main__':
    main();