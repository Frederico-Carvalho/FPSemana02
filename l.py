# Para Palavra

gualter = input()
len(gualter)
for i in set(gualter):
    a = gualter.count(i)
    print(a)

#Para Frase

gualter = input()
for i in gualter:
    a = gualter.count(i)
    print(gualter.split(i))