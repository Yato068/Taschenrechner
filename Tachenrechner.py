import importlib
#import Rechner
import cmath

while True:
    try:
        # Eingabe der Rechenart zuerst
        rechenart = input("Gib die Rechenart an (+, -, *, /, **, . für Wurzel, 'PS' für Prozentwert, 'GW' für Grundwert, 'PW' für Prozenzentsatz): ")

        # Überprüfung der Rechenart
        if rechenart not in ["+", "-", "*", "/", "**", ".", "wurzel", "PW", 'GW', 'PS']:
            print("Ungültige Rechenart. Bitte versuche es erneut.")
            continue  # Neustart der Schleife, um eine neue Eingabe zu ermöglichen

        # Abfrage der ersten Zahl
        if rechenart in ["PS", "PW"]:
            zahl_1 = complex(input("Gebe den Grundwert an: "))

        elif rechenart in ["GW"]:
            zahl_1 = complex(input("Gib den Prozuentwert an: "))

        else:
            zahl_1 = complex(input("Gib die erste Zahl an (z.B. 1+2j für komplexe Zahlen): "))

        # Variable zum Speichern des Ergebnisses
        ergebnis = 0

        # Grundrechenarten
        if rechenart == "+":
            zahl_2 = complex(input("Gib die zweite Zahl an (z.B. 1+2j für komplexe Zahlen): "))
            ergebnis = zahl_1 + zahl_2

        elif rechenart == "-":
            zahl_2 = complex(input("Gib die zweite Zahl an (z.B. 1+2j für komplexe Zahlen): "))
            ergebnis = zahl_1 - zahl_2

        elif rechenart == "*":
            zahl_2 = complex(input("Gib die zweite Zahl an (z.B. 1+2j für komplexe Zahlen): "))
            ergebnis = zahl_1 * zahl_2

        elif rechenart == "/":
            zahl_2 = complex(input("Gib die zweite Zahl an (z.B. 1+2j für komplexe Zahlen): "))
            if zahl_2 != 0:
                ergebnis = zahl_1 / zahl_2
            else:
                print("Division durch Null ist nicht erlaubt.")
                continue  # Neustart der Schleife, um eine neue Eingabe zu ermöglichen

        # Potenzoperation mit mehreren Zahlen (komplexe Potenz)
        elif rechenart == "**":
            zahl_2 = complex(input("Gib die zweite Zahl an (z.B. 1+2j für komplexe Zahlen): "))
            zahl_3 = complex(input("Gib die dritte Zahl an (z.B. 1+2j für komplexe Zahlen): "))
            zahl_4 = complex(input("Gib die vierte Zahl an (wenn nicht gebraucht, gib 1 an): "))
            # Berechnung der Potenzen mit ** für komplexe Zahlen
            ergebnis = cmath.exp(cmath.log(zahl_1) * zahl_2) ** zahl_3 ** zahl_4  # Komplexe Potenz

        # Wurzelberechnung
        elif rechenart == ".":
            if zahl_1 != 0:
                ergebnis = cmath.sqrt(zahl_1)  # Komplexe Wurzelberechnung
            else:
                print("Wurzelziehen mit einer Null ist nicht möglich.")
                continue

        # Wurzelberechnung speziell für eine negative Zahl
        #elif rechenart.lower() == "wurzel":
        #    ergebnis = cmath.sqrt(zahl_1)  # Berechnung der Wurzel (komplexe Wurzel von zahl_1)

        elif rechenart == "PS":
            zahl_2 = complex(input("Gib den Prozentwert an: "))
            ergebnis = (zahl_2 * 100) / zahl_1

        elif rechenart == "GW":
            zahl_3 = complex(input("Gib den Prozentsatz an: "))
            ergebnis = (zahl_1 * 100) / zahl_3

        elif rechenart == "PW":
            zahl_3 = complex(input("Gib den Prozentsatz an: "))
            ergebnis = (zahl_1 * zahl_3) / 100


        # Ausgabe des Ergebnisses
        if rechenart == "PS":
            print("Ergebnis: ", ergebnis,"%")
        else: print("Ergebnis: ", ergebnis)

    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine Zahl im richtigen Format ein.")
    except Exception as e:
        print(f"Es gab einen Fehler: {e}")

    # Modul neu laden (mein_rechner3)
    #importlib.reload(Rechner)
