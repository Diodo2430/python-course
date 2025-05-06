numeros=[15,78,89,25,64,74,12]
todos_validos=True

for numero in numeros:
    if not (numero >0 and numero < 100):
        todos_validos= False
    break
if todos_validos:
    print("Todos os numeros são positivos e maiores que 100")

else:
    print("Todos os numeros não são válidos e menores que 100")
