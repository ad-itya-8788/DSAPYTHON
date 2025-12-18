import re

pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&~])[A-Za-z\d@$!%*?&~]{8,}$')

passwords = ["Passwords123!", "Bandi007", "Bond@007"]

for pwd in passwords:
    if pattern.match(pwd):
        print(f"{pwd} is valid")
    else:
        print(f"{pwd} is invalid")
