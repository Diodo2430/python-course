def celsius_fahrenheit ():
    get_temp_celsius = float(input("Insira a temperatura em celsius: "))
    convert_fah = (get_temp_celsius * 1.8) + 32
    return convert_fah

temp_fah = celsius_fahrenheit()

print(f"A trmperatura em fahrenheit é {temp_fah}: ")

def fahrenheit_celsius ():
    get_temp_farenheit = float(input("Insira a temperatura em fahrenheit: "))
    convert_celsius = (get_temp_farenheit - 32) * 5/9
    return convert_celsius

temp_cel = fahrenheit_celsius()

print(f"A temperatura em celsius é: {temp_cel}")