BASE = 65

def caesar_cipher(message, key):
    key_as_num = convert_char_to_number(key)
    print(key_as_num)

def convert_char_to_number(key):
    return ord(key) - BASE

def watch(number, mod):
    return number % mod

def long_welcome():
    print("Bienvenido al palacio de Caesar, competencia de la casa de Toño.")

lista = [3, 5, 9, 20]
max_value = max(lista)

def quiero_que_el_maximo_valor_sea(valor, lista):
    maximo = max(lista)
    if maximo == valor:
        return f"{valor} si es el máximo en la lista"
    return f"{valor} no es el máximo valor en la lista"

mis_campeones = [6, 2, 4, 8, 5]
mi_preferido = 20
es_maximo = quiero_que_el_maximo_valor_sea(mi_preferido, mis_campeones)
print(es_maximo)
