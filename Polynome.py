import numpy as np

# Polynome definieren als Liste der Koeffizienten
# Beispiel: 3x^2 + 2x + 1 wird als [3, 2, 1] eingegeben
def berechne_polynom(coeff, x):
    # numpy.polyval wertet das Polynom für einen gegebenen x-Wert aus
    ergebnis = np.polyval(coeff, x)
    return ergebnis

# Beispielanwendung
if __name__ == "__main__":
    # Koeffizienten des Polynoms eingeben
    coeff = [3, 2, 1]  # Entspricht dem Polynom 3x^2 + 2x + 1
    x = 5  # Der x-Wert, für den das Polynom ausgewertet werden soll

    ergebnis = berechne_polynom(coeff, x)
    print(f"Das Ergebnis des Polynoms für x={x} ist {ergebnis}.")
