import re

def vocal(word):
    n = 0
    vocales = "aeiou"
    for letra in vocales:
        if letra in word:
            n += word.count(letra)
    return n

def twice(word):
    for letra in word:
        if letra+letra in word:
            return True
    return False

def ban(word):
    bw = ["ab","cd","pq","xy"]
    for par in bw:
        if par in word:
            return True
    return False

def nice(word):
    if ban(word):
        return False
    if vocal(word) < 3:
        return False
    if not twice(word):
        return False
    return True

def repet2(word):
    if len(re.findall(r"([a-z]).\1", word)) >= 1:
        return True
    return False

def twice2(word):
    for letra1 in word:
        for letra2 in word:
            if word.count(letra1+letra2) >= 2:
                return True
    return False


def nice2(word):
    if repet2(word) and twice2(word):
        return True
    return False

nicew = 0
with open("input.txt") as archivo:
    for linea in archivo:
        if nice2(linea):
            nicew += 1

print(nicew)
input()
