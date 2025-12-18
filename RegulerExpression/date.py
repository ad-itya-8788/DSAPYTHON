import re
text="12/12/2024 is celebrate xyz day and 01/04/2025 was internation dog day"
result=re.findall(r"\b\d{2}/\ d{2}/\d{4}\b",text)
print(result)