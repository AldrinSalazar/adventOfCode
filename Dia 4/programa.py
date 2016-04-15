import hashlib

inicio = "ckczppom"
num = 0

while True:
    h = hashlib.md5((inicio+str(num)).encode("utf-8")).hexdigest()
    if h.startswith("000000"):
        break
    num +=1

print(num)
