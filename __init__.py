a = 0
b = 1


n = int(input("Entrez le nombre de termes de la suite : "))

suite = []

for i in range(n):
    suite.append(a)
    a, b = b, a + b


print("Résultat :", ", ".join(map(str, suite)))
