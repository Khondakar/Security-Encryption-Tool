from cryptography.fernet import Fernet


def make_key(keyName):
    key = Fernet.generate_key()
    file = open(keyName, 'wb')
    file.write(key)
    file.close()


def encrypt_file(clearFileName, encFileName, keyFile):
    file = open(keyFile, 'rb')
    key = file.read()
    file.close()

    input_file = clearFileName
    output_file = encFileName

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)


def decrypt_file(encFileName, clearFileName, keyFile):
    file = open(keyFile, 'rb')
    key = file.read()
    file.close()

    input_file = encFileName
    output_file = clearFileName

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
