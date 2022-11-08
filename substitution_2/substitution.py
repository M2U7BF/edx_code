# 置換暗号のプログラム
import sys

args = sys.argv

if len(args) == 1:
    raise Exception("Usage: python substitution.py key")

encryption_key = args[1]

if len(encryption_key) < 26:
    raise Exception("Keys must contain 26 characters")
# 暗号キーを全て大文字に変換
encryption_key = [chr(ord(letter)-32) if 122 >= ord(letter) >= 97 else letter for letter in encryption_key]

def encrypt(plaintext):
    ciphertext = ""
    for letter in plaintext:
        index = 0

        if 90 >= ord(letter) >= 65:
            # 大文字の場合
            index = ord(letter) - 65
            ciphertext += encryption_key[index]
        elif 122 >= ord(letter) >= 97:
            # 小文字の場合
            index = ord(letter) - 97
            # 暗号キーを小文字に変換する
            ciphertext += chr(ord(encryption_key[index]) + 32)
        else:
            ciphertext += letter

    return ciphertext


plaintext = input("plaintext :")
print("ciphertext :"+encrypt(plaintext))

# テスト
def encrypt_check():
    ciphertexts = []

    encryption_key = "VCHPRZGJNTLSKFBDQWAXEUYMOI"
    ciphertexts.append(encrypt("hello C45r"))
    standard = encrypt("hello C45r")

    encryption_key = "vchprzgjntlskfbdqwaxeuymoi"
    ciphertexts.append(encrypt("hello C45r"))
    encryption_key = "VcHpRzGjNtLsKfBdQwAxEuYmOi"
    ciphertexts.append(encrypt("hello C45r"))

    for ciphertext in ciphertexts:
        if(ciphertext != standard):
            raise Exception("Error")

encrypt_check()