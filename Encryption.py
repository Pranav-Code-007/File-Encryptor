from cryptography.fernet import Fernet
fernet = Fernet(b'J64ZHFpCWFlS9zT7y5zxuQN1Gb09y7cucne_EhuWyDM=')


def encrypt(filename):
    with open(filename, 'rb') as file:
        original = file.read()

# encrypting the file
    encrypted = fernet.encrypt(original)
    with open(filename+'.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(filename):
    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    filename = filename.removesuffix(".enc")
    with open(filename, 'wb') as dec_file:
        dec_file.write(decrypted)

# encrypt("aaj.txt")
# decrypt("aaj.txt.enc")