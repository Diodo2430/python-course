data_user = {
    "Harley-Davison Iron 883 preta": 2014,
    "Suzuki Boulevar M109R preta": 2024,
    "Yamaha NIKEN-GT preto": 2023,
}

print("Interando sobre chaves e acessando valores")
for nome in data_user:
    car = data_user[nome]
    print(f"nome:{nome}, car:{car}")