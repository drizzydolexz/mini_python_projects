from cryptography.fernet import Fernet #module for encryption
import getpass #this hides the password when the user enters it
import random
import string

'''
 key + password + text to encrypt = random text
 random text + key+ password = text to encrypt
create two function one to generate key and one to store the key
'''
#function to create key
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

#function to read key
def load_key():
    return open("key.key","rb").read()

def initialize():
    #checks if function exists, if not,generate a new key
    try:
        load_key()
    except FileNotFoundError:
        print("Key file not found. Generating a new key")
        write_key()
        
def generate_random_password():
    length =random.randint(12, 16)
    characters = string.ascii_letters +string.digits +string.punctuation
    return ''.join(random.choice(characters) for i in range (length))

initialize()

master_pwd = getpass.getpass("What is your master password? ")#hides password upon entry
key = load_key() + master_pwd.encode() 
cipher_suite = Fernet(key)

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.strip()
            username, encrypted_password = data.split("|")
            decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
            print("username:", username, "password:", decrypted_password)

def add ():
    name = input("Username: ")
    generate_random = input("Do you want to generate random password?")

    if generate_random.lower() == "yes":
        pwd = generate_random_password()
        print("Generated Password:", pwd)
    else:
        pwd = getpass.getpass("Enter the Password: ")
    
    encrypted_pwd = cipher_suite.encrypt(pwd.encode()).decode()

    with open( "password.txt", 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")# takes the password convert it to byte using the encode() and encrypts it with fer.encrypt() and decode it


while True:
    print("\n1. View Passwords\n2. Add Paasword\n3. Quit")
    choice = input("Enter your choice (1/2/3): ")
    if  choice == "q" or choice == "quit" or choice == "3":
        break

    if choice == "view" or choice == "1" :
        view()
    
    elif choice == "add" or choice == "2":
        add()
        
    else:
        print("please enter 1,2, or 3. or view, add or quit or q")
