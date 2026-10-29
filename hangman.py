import random

geheim_wort = ["Andrej", "Ernis", "Finn", "Adam", "Safal", "Fabio", "Levin", "Nico"]

zufall_geheimes_wort = random.choice(geheim_wort).lower()

buchstaben_geheime_wort = list(zufall_geheimes_wort)

unterstrich_anzahl = ["_"] * len(zufall_geheimes_wort)

print(" ".join(unterstrich_anzahl))
fail = 0

while fail < 6:
    input_buchstabe = input("Gib einen Buchstaben ein: ")
    gefunden = False

    for i in range(len(buchstaben_geheime_wort)):
        if buchstaben_geheime_wort[i] == input_buchstabe:
            unterstrich_anzahl[i] = input_buchstabe
            gefunden = True

    if gefunden:
        print(" ".join(unterstrich_anzahl))
    else:
        print("Fehler: " + str(fail))
        fail += 1

print("Game Over! Das geheime Wort war: " + zufall_geheimes_wort)