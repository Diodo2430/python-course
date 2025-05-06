numeros=[]
for numero in range(5):

    
    entrada =float(input("Insira um numero:"))
    numeros.append(entrada)


    if not (numero >0 and numero < 100):
        todos_validos= False
    break
if todos_validos:
    print("Todos os numeros são positivos e maiores que 100")

else:
    print("Todos os numeros não são válidos e menores que 100")
