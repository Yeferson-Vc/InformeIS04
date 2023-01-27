#Escribir una función que determine la longitud de la
#subcadena más larga que no contiene ninguna letra
#repetida.
def  palabra( palabras ):
    palabra_longitud  = []
    for  p  in  palabras :
        palabra_longitud.append(( len ( p ), p ))
    
    palabra_longitud.sort()

    return  palabra_longitud [ - 1 ][ 1 ]


palabras  = [ 'chabelos' , 'coldplay' , 'thebealtles' , 'queen' ]

print(palabra( palabras ))

