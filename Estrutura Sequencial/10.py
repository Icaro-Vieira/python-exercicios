"""
    Faça um Programa que peça a temperatura em graus Celsius, 
    transforme e mostre em graus Fahrenheit.
"""

import math

print("Graus Celsius (°C) para Graus Fahrenheit (°F)")

graus_celsius = float(input("Insira a temperatura em Graus Celsius (°C): "))
graus_fahrenheit = (graus_celsius * 9 / 5) + 32

print(f"{graus_celsius}°C em Graus Fahrenheit é {round(graus_fahrenheit, 2)}°F")

