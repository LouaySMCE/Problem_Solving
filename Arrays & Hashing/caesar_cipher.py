def caesar_crypt(s, param):
    t = ""
    l1 = []
    l2 = []
    base = ord("A")
    for elm in s:
        l1.append(ord(elm))
    for num in l1:
        num = num + param
        if num > ord("Z"):
            num = num - 26
        if num < base:
            num = num + 26
        l2.append(chr(num))
    for char in l2:
        t = t+char
    return t
#print(caesar_crypt("VENIVIDIVICI",3))

def caesar_decrypt(s, param):
    mot = caesar_crypt(s, -param)
    return mot

def intercept(s):
    for i in range(26):
        print(i,caesar_decrypt(s,i))

#print(caesar_decrypt("A",3))
#intercept("AVJLZJRCREKLIZEXZEMVEKVLIDVTFEELULKVJKUVKLIZEX")

"""
def vegenere(s, key):
    l1 =[]
    l2 = []
    n = len(s) / len(key)
    m = len(s) // len(key)
    for k in range(len(key)):
        l1.append(k)
    for elm in s:
        if len(l1)< s:
            l1.append()
    return l1
print(vegenere("reddeadredemptionz", "hellow"))
"""
