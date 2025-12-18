import re
text="call us on 1234567809 or 9876543210 or 4567890124"
result=re.findall(r"\b\d{10}\b",text)
print(result)

'''\b means before space in netween digit \b matlab after space'''