nb = float(input("Entre le nombre : "))
x = nb
for i in range(1, int(nb)):
    if (i**2-nb < x):
        x = i
for i in range(1, 10):
    x = (nb/x + x)/2
print(f"La racine carree de {nb} est : {x}")