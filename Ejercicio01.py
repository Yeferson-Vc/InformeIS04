#Escribir una función que determine si una cadena es un
#palíndromo (se lee igual en ambos sentidos) o no:

def palindromo(cadena):
    p_izquierda = 0
    p_derecha = len(cadena) -1
    while p_derecha >= p_izquierda:
        if not cadena[p_izquierda] == cadena[p_derecha]:
            return False
        p_izquierda += 1
        p_derecha +=1

        return True
print(palindromo("ana"))
print(palindromo("sayas"))
print(palindromo("yeferson"))