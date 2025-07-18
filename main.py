#!/usr/bin/env python3

"""
Example module for linting and testing
"""

import string


def encode(word):
    encoded = ""
    for letter in word:
        if letter == " ":
            encoded = encoded + " "
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letters[x]
    return encoded


def decode(word):
    decoded = ""
    for letter in word:
        if letter == " ":
            decoded = decoded + " "
        else:
            x = letters.index(letter) - shift
            decoded = decoded + letters[x]
    return decoded


shift = 3
letters = string.ascii_letters + string.punctuation + string.digits


def main():
    choice = input("would you like to encode or decode?")
    word = input("Please enter text")
    output = ""
    if choice == "encode":
        output = encode(word)
    if choice == "decode":
        output = decode(word)

    print(output)


if __name__ == "__main__":
    main()
