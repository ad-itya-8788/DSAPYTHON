class underage(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message=message
x=int(input("Enter number:"))
try:
    if x<18:
        raise underage("Age Must be 18 or above")
except underage as age:
    print("Error Msg:",age.message)
else:
    print("Age is Appropriate")