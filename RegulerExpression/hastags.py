import re
text="learning #Neworking #Python and os is fun"
hastags=re.findall(r"#\w+",text)
print(hastags)