
from consts import ABC

def main():
    key = 3
    plaintext = 'za'
    c = caesar_cipher(plaintext, key)
    p = caesar_cipher(c, key * -1)
    print(f'caesar_cipher p: {p}, c: {c}')
    
    c = atbash_cipher(plaintext)
    p = atbash_cipher(c)
    print(f'atbash_cipher p: {p}, c: {c}')

def caesar_cipher(m, k):
    c = ''
    for char in m:
        c += ABC[(ABC.index(char) + k) % 26]
    return c

def atbash_cipher(m):
    c = ''
    for char in m:
        c += ABC[len(ABC) - ABC.index(char) - 1]
    return c

if __name__ == "__main__":
    main()