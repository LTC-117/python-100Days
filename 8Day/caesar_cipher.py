import art

def caesar(message, shift, direction):
    if direction not in ("encode", "decode"):
        return "error"


    if direction == "decode":
        shift *= -1

    result = "".join(
        chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        if letter.islower() else letter
        for letter in message
    )

    return result
    

print(art.logo)

user_entry = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
msg = input("Type your message:\n")
shift_num = int(input("Type the shift number:\n"))

res = caesar(msg, shift_num, user_entry)

print(f"result -> {res}")
