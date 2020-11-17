from consts import ABC
import matplotlib.pyplot as plt

def main():
    frequency_dict = {}
    for letter in ABC:
        frequency_dict[letter] = 0

    with open('text.txt', 'r') as f:
        for line in f:
            for char in line.lower():
                if char in ABC:
                    frequency_dict[char] += 1

    print(frequency_dict)
    plt.bar(*zip(*frequency_dict.items()))
    plt.show(frequency_dict)

if __name__ == "__main__":
    main()