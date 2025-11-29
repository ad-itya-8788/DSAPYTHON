🚀 File Handling in Python – Full Guide (Zero to Expert)

1. What is File Handling?
👉 File handling ka matlab hai Python program ke through external files ko create, read, update aur delete karna.

File types ho sakte hai:

Text files → .txt, .csv, .log

Binary files → .jpg, .mp4, .exe


2. Why We Do File Handling? (Necessity)
Pehle programming mai jo data hota tha wo temporary memory (RAM) mai hota tha.

Program close → Data gayab ❌

File handling se:
Data hard disk (permanent storage) mai store hota hai

Next time bhi use kar sakte ho

Large data handle karna easy hota hai

3. Advantages of File Handling

✅ Permanent storage of data (program close hone ke baad bhi data bacha rehta hai).

✅ Data sharing easy (file share karke dusre ko bhej sakte ho).

✅ Large data management possible (jaise student records, logs).

✅ Automation (reports generate karna, read/write without manual entry).

✅ Different formats support (text, csv, binary, images, pdf).

4. Disadvantages

❌ Agar file corrupt ho gayi → data lost.

❌ File handling slow hoti hai DBMS (database) ke comparison mai.

❌ Data security low (plaintext mai store hota hai).

❌ Concurrency (multiple users ek sath file access) difficult hota hai.

5. What We Did Before File Handling?

👉 Pehle data store karne ke liye:

Variables (sirf runtime ke liye)

Arrays / Lists (program ke andar hi data)

Databases (heavy aur complex cheezon ke liye)

⚡ Lekin chhote programs mai file handling best hai (simple + lightweight).

6. File Open Modes in Python
Mode	Meaning	Behavior
r	Read	File open for reading (error agar file nahi hai)
w	Write	File create karega, agar file pehle hai to overwrite karega
a	Append	File end mai add karega, overwrite nahi karega
x	Exclusive	File create karega, agar file hai to error
b	Binary	Binary mode (images, videos)
t	Text	Default mode (text files)
r+	Read + Write	File open karega, overwrite karega starting se
w+	Write + Read	File overwrite karega aur read bhi kar sakte ho
a+	Append + Read	File end mai add karega aur read bhi kar sakte ho
7. Basic Functions in File Handling
Function	Use
open()	File open karne ke liye
read()	Entire file read
readline()	Ek line read
readlines()	Sab lines list ke form mai read
write()	String file mai likhne ke liye
writelines()	Multiple lines likhne ke liye
close()	File band karne ke liye
seek()	Cursor ko specific position pe le jana
tell()	Current cursor position batana
flush()	Buffer clear karke data immediately likhna
8. Examples (Step by Step)
(a) Write into a file
f = open("demo.txt", "w")
f.write("Hello Aditya!\n")
f.write("This is file handling in Python.\n")
f.close()

(b) Read file (full)
f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()

(c) Read line by line
f = open("demo.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(line1, line2)
f.close()

(d) Read all lines into list
f = open("demo.txt", "r")
lines = f.readlines()
print(lines)
f.close()

(e) Append data
f = open("demo.txt", "a")
f.write("Appending more content!\n")
f.close()

(f) Read + Write mode
f = open("demo.txt", "r+")
print("Before:", f.read())
f.write("Added via r+ mode!\n")
f.close()

(g) Working with cursor (seek/tell)
f = open("demo.txt", "r")
print(f.read(5))   # read 5 chars
print("Cursor at:", f.tell())
f.seek(0)          # move to start
print(f.read())
f.close()

(h) With statement (best practice)
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# no need to close(), auto handled

(i) Binary file read
with open("pic.jpg", "rb") as f:
    data = f.read(20)
    print(data)   # first 20 bytes

9. Cross Questions (Interview Style)

❓ Q1: Difference between w and a mode?
👉 w overwrite karega, a append karega.

❓ Q2: What if file doesn’t exist in r mode?
👉 Error aayega (FileNotFoundError).

❓ Q3: What is difference between read(), readline() and readlines()?
👉 read() → pura content ek string mai
👉 readline() → ek line
👉 readlines() → list of lines

❓ Q4: Why use with open() instead of open()?
👉 Kyunki yeh auto close kar deta hai, memory leaks avoid hote hai.

❓ Q5: Can we write integers directly into file?
👉 Nahi, sirf strings likh sakte ho. Int ko str() me convert karna padega.

❓ Q6: Difference between text mode t and binary mode b?
👉 Text mode → human readable (UTF-8 encoding)
👉 Binary mode → raw bytes (images, video).