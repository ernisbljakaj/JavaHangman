import random

geheim_wort = ["Andrej", "Ernis", "Finn", "Adam", "Safal", "Fabio", "Levin", "Nico"]

zufall_geheimes_wort = random.choice(geheim_wort)



unterstrich = " _ "
unterstrich_anzahl = len(zufall_geheimes_wort) * unterstrich

buchstaben_geheime_wort = list(zufall_geheimes_wort)

print(unterstrich_anzahl)
fail = 0


while fail < 6:

    input_buchstabe = input("Gib einen Buchstaben ein: ")
    print("Fehler: ", fail)
    for i in range(len(buchstaben_geheime_wort)):
        i=0
        if buchstaben_geheime_wort[i] == input_buchstabe:
            unterstrich_anzahl[i] = input_buchstabe
            print(unterstrich_anzahl)
        else:
            fail += 1
            
    
