import random

geheim_wort = ["Andrej", "Ernis", "Finn", "Adam", "Safal", "Fabio", "Levin", "Nico"]

zufall_geheimes_wort = random.choice(geheim_wort)

unterstrich = " _ "
unterstrich_anzahl = len(zufall_geheimes_wort) * unterstrich

buchstaben_geheime_wort = list(zufall_geheimes_wort)

print(unterstrich_anzahl)

unterstrich_anzahl = list(unterstrich_anzahl)


