#Caesar Cipher
print("Welcome to Caesar Cipher!")
e_or_d = str(input("Do you wish to encrypt or decrypt a message?\n")).lower()
if not e_or_d == "encrypt" and not e_or_d == "decrypt":
    print("Error: Invalid input.")
    exit()
message = str(input(f"What is the message you would like to {e_or_d}?\n")).lower()
shift = int(input("How many characters would you like to shift the message by?\n"))
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(m:str, s:int, encode_or_decode:str):
    if encode_or_decode == "encode":
        encrypted_message = ""
        for l in m:
            if not l.isalpha():
                encrypted_message += l
                continue
            index = characters.index(l)
            if index + s > len(characters) - 1:
                index -= len(characters)
            encrypted_message += characters[index + s]
        return encrypted_message
    elif encode_or_decode == "decode":
        decrypted_message = ""
        for l in m:
            index = characters.index(l)
            if index - s < 0:
                index += len(characters)
            elif not l.isalpha():
                decrypted_message += l
                continue
            decrypted_message += characters[index - s]
        return decrypted_message
    else:
        print("Error: Invalid input")
        return ""

print(f"Your {e_or_d}ed message is: {caesar_cipher(message, shift, "encode")}")