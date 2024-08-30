def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

entrada = input("Informe uma string: ")
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")