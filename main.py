from translator import Translator
from dictionary import Dictionary


dictionary = Dictionary.from_char_to_morse_json("char_to_morse.json")
translator = Translator(dictionary)

print("Morse Code Encoder/Decoder")
print("-"*20)
running = True
while running:
    print("You have two options:\n1. Encode a string of characters into morse code." +
          "\n2. Decode a morse code string into a string of characters.")
    encode_or_decode = input("Would you like to encode or decode? [encode/decode]: ")

    if encode_or_decode.lower() == "encode":
        string = input("Please enter your string: ")
        print("Here is your encoded string:")
        print(translator.encode_char_string(string))

    elif encode_or_decode.lower() == "decode":
        string = input("Please enter your string: ")
        print("Here is your decoded string:")
        print(translator.decode_morse_string(string))

    else:
        print("Invalid option. Please choose either 'encode' or 'decode'.")
        continue

    if input("Enter 'exit' to exit or press anything else to continue: ").strip().lower() == "exit":
        running = False
