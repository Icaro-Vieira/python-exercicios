'''
    Faça um Programa que calcule a área de um quadrado, 
    em seguida mostre o dobro desta área para o usuário.
''' 
print("**** Dobro da Área de um quadrado ****")
lado = int(input("Informe o tamanho de uma aresta: "))

area = lado * lado
dobro = area * 2

print(f"A area é = {area} O dobro da area do quadrado é {dobro}")