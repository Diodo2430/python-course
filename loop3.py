i = 0
produtos_eletronicos= ["aparelho celular", "macbook", "computador", "servidor", "teclado", "televisao", "monitor"]
for i in produtos_eletronicos:
    print(i)
add = produtos_eletronicos.append("fone de ouvido")
print(produtos_eletronicos)    
exclude = produtos_eletronicos.pop()
print(produtos_eletronicos)
print(len(produtos_eletronicos))