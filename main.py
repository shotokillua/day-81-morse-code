morse = {"a": ".-",
         "b": "-...",
         "c": "-.-.",
         "d": "-..",
         "e": ".",
         "f": "..-.",
         "g": "--.",
         "h": "....",
         "i": "..",
         "j": ".---",
         "k": "-.-",
         "l": ".-..",
         "m": "--",
         "n": "-.",
         "o": "---",
         "p": ".--.",
         "q": "--.-",
         "r": ".-.",
         "s": "...",
         "t": "-",
         "u": "..-",
         "v": "...-",
         "w": ".--",
         "x": "-..-",
         "y": "-.--",
         "z": "--..",
         " ": " ",
         }
string = input("Type something to convert it to morse code: ").lower()


def text_to_morse():
    morse_string = ""
    for i in string:
        morse_string += morse[i]
    print(morse_string)

text_to_morse()