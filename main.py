# DICTIONARY TO CREATE KEY:VALUE PAIRS
morse = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}


# FUNCTION FOR USER TO INPUT
def morse_code(usr_input):

    # EMPTY VARIABLE TO ADD THE TRANSLATED INPUT INTO
    morse_output = ""

    # FOR LOOP TO ITERATE THROUGH THE USERS INPUT
    for letter in usr_input:

        # ADD MORSE CODE USER INPUT TO EMPTY VARIABLE WITH A SPACE IN BETWEEN FOR CLARITY
        morse_output += morse[letter] + " "
    return f"{usr_input} in Morse Code is {morse_output}"


print(morse_code(input("What would you like to translate?\n").upper()))
