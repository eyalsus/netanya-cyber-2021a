from consts import ABC
from viz import plot_dict_as_bar_chart
from symmetric_ciphers import caesar_cipher, vigenere_cipher
def main():
    with open('text.txt', 'r') as f:
        text = f.read()
    
    # freq = get_letters_frequency(text)
    # print(freq)
    # plot_dict_as_bar_chart(freq)
    ciphertext = caesar_cipher(text, 3)
    freq = get_letters_frequency(ciphertext)
    print(freq)
    plot_dict_as_bar_chart(freq)

def get_letters_frequency(text):
    frequency_dict = {}
    for letter in ABC:
        frequency_dict[letter] = 0

    for char in text.lower():
        if char in ABC:
            frequency_dict[char] += 1

    return frequency_dict

if __name__ == "__main__":
    main()