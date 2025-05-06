data_user = {
    "Hugo": 20, 
    "Arthur": 20,
    "Antonio": 21,
}

print("Iterarando sobre chaves e acessando valores:")
for nome in data_user:
    idade = data_user[nome]
    print(f"nome: {nome}, Idade: {idade}")