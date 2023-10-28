"""Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Sabemos que:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes"""

a = int(input('Digite o lado 1 do triangulo: '));
b = int(input('Digite o lado 2 do triangulo: '));
c = int(input('Digite o lado 3 do triangulo: '));

if (a + b < c) or (b + c < a) or (a + c < b):
    print('Nao e um triângulo!');
elif (a == b) and (a == c):
    print('Equilatero');
elif(a == b) or (a == c):
    print('Isólceles');
elif(a != b) or (b != c) or (c != a):
    print('Escaleno');