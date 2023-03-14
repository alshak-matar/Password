import re
import hashlib 


print(" 🤩 Hello, for a valid password, you need at least:")
print(" 👉 8 characters an uppercase letter and lowercase letter ")
print( " 👉 Number and special character ( %, ^, &, *, !, @, #, $)")

specials_characters = [ "$", "%", "^", "&", "*", "!", "@", "#" ]

while True: 
    passm = input("Enter your Password : ")
    if len(passm) <=8:
        print("Invalid 8 characters minimum please try again")
    elif passm == passm.upper():                                    
        print("Invalid At least one lowercase letter please try again")
    elif not re.search("[0-9]", passm):                         
        print("Invalid At least one number please try again")
    elif passm== passm.lower():                                   
        print("Invalid At least one capital letter please try again")
    elif not any(char in specials_characters for char in passm):
        print("Invalid At least one special character please try again") 
    else : 
        print("Valid password good job") 
        break
password=hashlib.sha256(passm.encode('utf-8')).hexdigest()
print("Here is your encrypted password: ", password)
