from cryptography.fernet import Fernet
import os

# the program will take 

class KeyGenerator():
    base_key = os.path.join(os.path.dirname(__file__), "secret.key")
    def __init__(self, password = None):
        self.password = password
        if not os.path.exists(self.base_key):
            self.generate_key()
        self.load_key()

    # if keyfile does not exist
    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.base_key, "wb") as key_file:
            key_file.write(key)
    
    def load_key(self):
        self.key = open(self.base_key, "rb").read()
        self.fernet_key = Fernet(self.key)
    
    # takes password and encrypt it
    def encrypt_key(self):  
        encode_password = self.password.encode("ascii")
        encoded_password = self.fernet_key.encrypt(encode_password)
        return encoded_password.decode("ascii")
    
    # function to decrypt content
    def decrypt_key(self):
        #takes a string and converts in bytes
        decode_password = self.password.encode("ascii")
        decrypted_password = self.fernet_key.decrypt(decode_password)
        return decrypted_password.decode("ascii")

if __name__ == "__main__":
    KeyGenerator()



