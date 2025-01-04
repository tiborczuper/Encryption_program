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

print(f"Megadott üzenet: {text}\n")
print(f"Titkosított üzenet:\n{encrypted_text}")
print(f"Titkosítási kulcs:\n{keystr}")