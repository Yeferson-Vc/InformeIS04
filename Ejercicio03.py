#Escribir una función que divida una cadena dada en una
#lista de subcadenas cada vez que aparezca un carácter
#específico.

def palabra(cadena):
    a = cadena.split("#",1)
    return a
print(palabra("lucho#robert#lois#"))