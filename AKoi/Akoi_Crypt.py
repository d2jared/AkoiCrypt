import secrets

cle = secrets.token_bytes(16)  # Génère une clé de 16 octets (128 bits)

def Encrypt(plainText, cle):
    plainText = plainText.encode() # Convertir le texte en octets
    cipherText = bytearray()
    for i in range(len(plainText)):
        byte = plainText[i] ^ cle[i%len(cle)]
        cipherText.append(byte)
    print("clé générée:", cle.hex())
    return cipherText.hex()

def Decrypt(cipherText, cle):
    cle = bytes.fromhex(cle)
    cipherText = bytes.fromhex(cipherText)
    plainText = bytearray()
    for i in range(len(cipherText)):
        byte = cipherText[i] ^ cle[i%len(cle)]
        plainText.append(byte)
    return plainText.decode()
