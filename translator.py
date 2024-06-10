from dictionary import Dictionary


class Translator:
    char_separator = " "
    word_separator = char_separator * 3

    def __init__(self, dict_: Dictionary):
        self.dictionary = dict_

    def encode_char_string(self, ch_string: str) -> str:
        encoded_string = ""

        for char in ch_string:
            if char == " ":
                encoded_string += Translator.word_separator
                # A word separator will always follow a char separator and so we undo the char separator to
                # have the correct spacing between words.
                encoded_string = encoded_string[:-len(Translator.char_separator)]
            else:
                encoded_string += self.dictionary.encode_char(char) + Translator.char_separator
        # The above loop will leave a trailing char separator on the encoded string.
        return encoded_string[:-1]

    def decode_morse_string(self, mo_string: str) -> str:
        decoded_string = ""

        for encoded_word in mo_string.split(Translator.word_separator):
            decoded_word = ""

            for encoded_char in encoded_word.split(Translator.char_separator):
                decoded_word += self.dictionary.decode_morse(encoded_char)
            decoded_string += decoded_word + " "

        return decoded_string


if __name__ == "__main__":
    test_str = "a string for testing the encoding and decoding into and from morse code"
    dictionary = Dictionary.from_char_to_morse_json("char_to_morse.json")
    translator = Translator(dictionary)

    morse_string = translator.encode_char_string(test_str)
    print(f"Here is a translation into morse code: \n{morse_string}")
    decoded_morse = translator.decode_morse_string(morse_string)
    print(f"And here is that morse code decrypted: \n{decoded_morse}")
