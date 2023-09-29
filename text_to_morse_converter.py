data = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
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
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}

morse_code = None


def morse_converter(text):
    m_code = ""
    for char in text:
        for m_char_key in data:
            if char == m_char_key:
                m_code += " " + data.get(m_char_key)
            elif char not in data:
                print("\nEntered text has unsupported characters.\n"
                      "Please remove it or find another converter that does it.")
                return None
    return m_code[1:]


print("\nWelcome to the Text to Morse Code Converter!\n")
while not morse_code:
    input_text = input("Enter the Text and hit enter to get the result\n(alphanumeric characters only): ").lower()
    morse_code = morse_converter(input_text)

print(f"Your text in Morse code is:\n{morse_code}\n")
