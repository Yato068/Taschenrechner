import numpy as np
import matplotlib.pyplot as plt
import importlib
import polynom_try

# Gegebene Daten vom Benutzer einlesen und in numpy-Arrays umwandeln
x = np.array([float(i) for i in input("Gib die x-Werte durch Kommas getrennt ein: ").split(',')])
y = np.array([float(i) for i in input("Gib die y-Werte durch Kommas getrennt ein: ").split(',')])

# Grad des Polynoms für die Anpassung
grade_of_fit = int(input("Gib den Grad des Polynoms ein: "))

# Polynom-Anpassung
coefficients = np.polyfit(x, y, grade_of_fit)

# Erzeugen der Polynomfunktion aus den Koeffizienten
poly_function = np.poly1d(coefficients)

# Generiere Werte für die Anzeige der Funktion
x_fit = np.linspace(min(x), max(x), 100)
y_fit = poly_function(x_fit)

# Plot der Daten und der Anpassung
plt.scatter(x, y, label='Datenpunkte')
plt.plot(x_fit, y_fit, label=f'Polynom-Anpassung (Grad {grade_of_fit})', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Polynom-Anpassung')
plt.grid(True)
plt.show()

importlib.reload(polynom_try)
# Ausgabe der Polynomformel
print(f'Die Polynomformel lautet: {poly_function}')
