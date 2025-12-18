import re
text="I am running ,eting adn playing"
result=re.findall(r"\w+(?=ing)",text)

print(result)
text1="Painting,Reading,Cooking,Markiing"
result1=re.findall(r"\w+(?=ing)",text1)
print(result1)



text2="Cat dog catalog category"
result=re.findall(r"cat(?!alog)",text)
print(result)

text="rate:Rs30 ,Profit:Rs2000,Loss:500"
result=re.findall(r"(?<=Rs)\d+",text)
print(result)
text="Email:info.imcc@mespune.in ,text.mastersoft@mesp.com"
result=re.findall(r"(?<=\b)\w+(?=@)",text)
print(result)