data_user = {
    "Fiat Uno Vivasi vermelho": 2015,
    "Hyundai Basic cinza": 2015,
    "Honda Civic cinza": 2020,
}

print("Interando sobre chaves e acessando valores")
for nome in data_user:
    car = data_user[nome]
    print(f"nome:{nome}, car:{car}")