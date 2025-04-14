# Password Generator
import string
import secrets

passlength = int(input("Enter the length of the password\n"))

letter = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
combine = letter + symbols + numbers

password = "".join(secrets.choice(combine) for i in range(passlength))

print(password)