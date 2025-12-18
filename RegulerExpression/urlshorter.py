import re

pattern = re.compile(
    r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\/.*)?$'
)

urls = [
    "https://www.codehub.in",
    "https://www.google.com"
]

for u in urls:
    if pattern.match(u):
        print(u, "is valid")
    else:
        print(u, "is invalid")
