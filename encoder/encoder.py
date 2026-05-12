alphabet = ["a", "b", "c", "d", "e", "f", "g", 
            "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", 
            "u", "v", "w", "x", "y", "z"]

def user_data():
    message = input("Message to encode: \n")
    process = input("Do you want to ENCODE or DECODE? \n").lower()
    encoding_number = int(input("Shift number? \n"))
    return message, process, encoding_number

def encode_message(message, process, encoding_number, alphabet):

    if process == "decode":
        encoding_number = -encoding_number
   
    word = []
    for letter in message:
        if letter not in alphabet:
            word.append(letter)
        else:
            letter_index = alphabet.index(letter) + encoding_number
            letter_index %= len(alphabet)
            new_letter = alphabet[letter_index]
            word.append(new_letter)
    return "".join(word)

while True:
    message, process, encoding_number = user_data()
    test = encode_message(message, process, encoding_number, alphabet)
    print(test)

    message = input("Do you want to continue YES = type 'y' | NO = type 'n': \n").lower()
    if message != "y":
        print("Goodbye!")
        break