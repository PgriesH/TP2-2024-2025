BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))
nfrom = (fromage * nbConvives) / BASE
neau = (eau * nbConvives) / BASE
nail = (ail * nbConvives) / BASE
npain = (pain * nbConvives) / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {nfrom} gr de fromage")
print(f"- {neau} dl d'eau")
print(f"- {nail} gousses(s) d'ail")
print(f"- {npain} gr de pain")
