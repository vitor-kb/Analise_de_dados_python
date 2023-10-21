#2) Fazer um programa para ler a distancia, valor do litro da gasolina, consumo do carro.

distancia = float(input('Digite a distancia percorrida do veiculo: '));

gasosa = float(input('Digite o valor do litro da gasolina: '));

consumo = float(input('Digite o valor de consumo do veiculo: '));

gasto_total = gasosa * (consumo * distancia);

print(f'Seu gasto será o equivalente a R$ {gasto_total}');