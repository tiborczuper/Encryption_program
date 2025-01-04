import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
keystr = ""
random.shuffle(key)
for v in key:
    keystr += v


#ENCRYPT
#NINCSENEK ÉKEZETES BETŰK!!!
text = input("Adj meg egy szöveget a titkosításhoz: ")
encrypted_text = ""

for letter in text:
     encrypted_text += key[chars.index(letter)]

print(f"Megadott üzenet: {text}")
print(f"Titkosított üzenet:")
print(encrypted_text)
print(f"Titkosítási kulcs:")
print(keystr)