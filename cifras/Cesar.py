import string

alfa = string.ascii_letters
def criptografia(frase, chave):
    frase_criptografada = ""
    chave = int(chave)

    for i in frase:
        if i.isalpha():
            base = ord('A') if i.isupper() else ord('a')
            frase_criptografada += chr((ord(i) - base + chave) % 26 + base)
        else:
            frase_criptografada += i 

    return frase_criptografada


def descriptografia(frase, chave):
    frase_descriptografada = ""
    chave = int(chave)
    for i in frase:
        if i.isalpha():
            base = ord('A') if i.isupper() else ord('a')
            frase_descriptografada += chr((ord(i) - base - chave) % 26 + base)
        else:
            frase_descriptografada += i
    return frase_descriptografada