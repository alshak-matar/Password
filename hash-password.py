import hashlib

def hash_password(password, salt):
    salted_password = password + salt

    encoded_password = salted_password.encode('utf-8')

    sha256_hash = hashlib.sha256(encoded_password)

    hashed_password = sha256_hash.hexdigest()

    return hashed_password
password = "my_password"
salt = "salty_salt"

hashed_password = hash_password(password, salt)

print(hashed_password)
