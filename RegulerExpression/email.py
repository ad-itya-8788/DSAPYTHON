import re
text="adityachav8788@gmail.com"
pattern=r"\b[a-zA-z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

result=re.findall(pattern,text)
print(result)