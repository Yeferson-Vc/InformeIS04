#Escribir una función que determine la frecuencia de cada
#carácter en una cadena dada y devuelva un diccionario.
texto = """Hola, mundo. quiero contarles que vivo preocupado sabiendo que lagún dia morire. Y es por eso que 
a veces no le encuentro sentido a la vida. Pero en fin hay a seguir dandole a la vida :c"""
quitar = ",;:.\n!\"'"
for caracter in quitar:
     texto = texto.replace(caracter,
                          "")
texto = texto.lower()
palabras = texto.split(" ")
print(palabras)