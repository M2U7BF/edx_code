import substitution

def encrypt_check():
    ciphertexts = []

    substitution.encryption_key = "VCHPRZGJNTLSKFBDQWAXEUYMOI"
    ciphertexts.append(substitution.encrypt("hello C45r"))
    standard = substitution.encrypt("hello C45r")

    substitution.encryption_key = "vchprzgjntlskfbdqwaxeuymoi"
    ciphertexts.append(substitution.encrypt("hello C45r"))
    substitution.encryption_key = "VcHpRzGjNtLsKfBdQwAxEuYmOi"
    ciphertexts.append(substitution.encrypt("hello C45r"))

    for ciphertext in ciphertexts:
        if(ciphertext != standard):
            raise Exception("Error")
