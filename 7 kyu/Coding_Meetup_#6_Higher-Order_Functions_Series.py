'''
7 kyu
Name: Password Hashes
https://www.codewars.com//kata/54207f9677730acd490000d1
Task: When you sign up for an account somewhere, some websites do not actually store your password in their databases.
 Instead, they will transform your password into something else using a cryptographic hashing algorithm.

After the password is transformed, it is then called a password hash. Whenever you try to login, the website will 
transform the password you tried using the same hashing algorithm and simply see if the password hashes are the same.

Create the function that converts a given string into an md5 hash. The return value should be encoded in hexadecimal.
'''

import hashlib

def pass_hash(str):
    res = hashlib.md5(str.encode())
    return res.hexdigest()