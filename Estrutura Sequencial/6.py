# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print("Calculadora Área de Circulo")
print("Formula para calcular a Área -> (A = π.r²)")

raio = float(input("Digite o Raio do Circulo: "))
pi = 3.1415926535898
area = pi * (raio**2)

print(f"O Área do circulo é A ≈ {area:.2f}²")