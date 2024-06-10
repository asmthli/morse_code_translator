from dictionary import Dictionary


class Translator:
    char_seperator = " "
    word_seperator = char_seperator * 3

    def __init__(self, dict_: Dictionary):
        self.dictionary = dict_

    def encode_char_string(self, ch_string: str) -> str:
        encoded_string = ""

        for ch in ch_string:
            if ch == " ":
                encoded_string += Translator.word_seperator
                # A word seperator will always follow a char seperator and so we undo the char seperator to
                # have the correct spacing between words.
                encoded_string = encoded_string[:-len(Translator.char_seperator)]
            else:
                encoded_string += self.dictionary.encode_char(ch) + Translator.char_seperator
        return encoded_string

    # def decode_morse_string(self, mo_string: str) -> str:
    #     decoded_string = ""
    #     for ch in mo_string:
    #         if ch == Translator.word_seperator:
    #             decoded_string += " "
    #         else:
    #             decoded_string += self.dictionary.decode_morse(ch)
    #     return decoded_string


if __name__ == "__main__":
    test_str = "a test string"
    dictionary = Dictionary.from_char_to_morse_json("char_to_morse.json")
    translator = Translator(dictionary)

    morse_string = translator.encode_char_string(test_str)
    print(morse_string)
