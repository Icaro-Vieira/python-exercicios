"""
    Faça um Programa que peça a temperatura em graus Fahrenheit, 
    transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9).
"""
import math

print("Graus Fahrenheit (°F) para Graus Celsius (°C)")

grau_fahrenheit = float(input("Insira a temperatura em Graus Fahrenheit (°F): "))
grau_celsius = 5 * ((grau_fahrenheit - 32) / 9)

print(f"{grau_fahrenheit}°F em Graus Celsius é {round(grau_celsius, 2)}°C")

