import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

encrypted_message = input("Add meg a titkosított üzenetet: ")
key = input("Add meg a titkosítási kulcsot: ")
decrypted_message = ""

for letter in encrypted_message:
    decrypted_message += chars[key.index(letter)]

print(chars)
print(key)
print(decrypted_message)