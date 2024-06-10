import json
import pprint


def invert_dict(dict_: dict):
    return {v: k for k, v in dict_.items()}


class Dictionary:
    def __init__(self, char_to_morse: dict, morse_to_char: dict):
        self.char_to_morse = char_to_morse
        self.morse_to_char = morse_to_char

    @classmethod
    def from_char_to_morse_json(cls, char_to_morse_json: str):
        with open(char_to_morse_json) as json_file:
            char_to_morse = json.load(json_file)

        morse_to_char = invert_dict(char_to_morse)
        return cls(char_to_morse, morse_to_char)

    @classmethod
    def from_morse_to_char_json(cls, morse_to_char_json: str):
        with open(morse_to_char_json) as json_file:
            morse_to_char = json.load(json_file)

        char_to_morse = invert_dict(morse_to_char)
        return cls(char_to_morse, morse_to_char)

    def encode_char(self, ch: str):
        return self.char_to_morse[ch]

    def decode_morse(self, morse: str):
        return self.morse_to_char[morse]


if __name__ == "__main__":
    dictionary = Dictionary.from_char_to_morse_json("char_to_morse.json")
    pprint.pp(dictionary.morse_to_char)

    print(f"Encoding of 'a' is {dictionary.encode_char('a')}.")
    print(f"This should read 'b': {dictionary.decode_morse(dictionary.encode_char('b'))}.")

