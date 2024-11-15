char = (input(" "))
dicionario = { }
for letra in char:
    if not letra.split():
        continue 
    if letra not in dicionario:
        dicionario[letra] = 1
    else:
         dicionario[letra] += 1 
print (dicionario)