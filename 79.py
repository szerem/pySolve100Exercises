import platform
import string

print(platform.python_version())

while True:
    psw = input('--> ') 
    if  any( i.isdigit() for i in psw) and any( i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
         print("Password is not fine")

