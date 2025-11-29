text = input("Enter text: ")
vowels = consonants = digits = special = 0
vowels_str = "aeiouAEIOU"
for ch in text:
    if ch.isalpha():
        if ch in vowels_str:
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch != ' ':
        special += 1
words = len(text.split())
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)
