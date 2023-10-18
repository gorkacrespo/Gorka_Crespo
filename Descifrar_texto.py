#PRE -> #Sustituir letra
#Sustituir letra en frase (Sustituir MAYUSCULA POR MINUSCULA)
#letra_org -> Mayuscula 
#letra_nueva -> Minuscula




frase = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE."""

frase_res = frase


#*******************Subprogramas****************
#Pasar de frase a diccionario de letras
def contar_apariciones_letras(frase):
    dic_letras = {}

    # Iterar a través de cada carácter en la frase
    for caracter in frase:
      
        # Verificar si el carácter es una letra
        if caracter.isalpha():
            # Si existe, incrementar su contador
            if caracter in dic_letras:
                dic_letras[caracter] += 1
            # Si no existe, agregarlo con un contador inicial de 1
            else:
                dic_letras[caracter] = 1

    return dic_letras



# Ordenar el diccionario de mayor a menor según los valores
def ordenar_apariciones_letra(dic_sin_ord):
    diccionario_ordenado = dict(sorted(dic_sin_ord.items(), key=lambda item: item[1], reverse= True))
    return diccionario_ordenado

#Eliminar letra
def eliminar_letra(lista, letra):
    if letra in lista:
        lista.remove(letra)

#Agragar elemento en diccionario (Solucion_claves)
def agregar_elemento(diccionario, clave, valor):
    diccionario[clave] = valor
    return diccionario


#**********************FIN SUBPROGRAMAS************************





#*************inicializacion*******************
#Diccionario con las probabilidades de que salga cada letra al escribir
L_max_prob = ["e","a","o","l","s","n","d","r","u","i","t","c","p","m","y","q","b","h","g","f","v","j","ñ","z","x","k","w"]
L_max_prob_copia = L_max_prob
x = 1
Solucion_claves = {}
#**********************************************






#Contamos apariciones
dic_l = contar_apariciones_letras(frase)
print("")
print("Apariciones letras")
print(dic_l)


#ordenamos
dic_ordenado = ordenar_apariciones_letra(dic_l)
print("")
print ("Ordenamos letras de may a menor")
print(dic_ordenado)


#Cambiar todas las letras por sus correspondientes teniendo en cuenta la probabilidad
#convertimos el diccionario a una lista de claves (Mayusculas)
claves_lista_ord = list(dic_ordenado.keys())
print("")
print("lista claves")
print(claves_lista_ord)


#obtener las palabras con 2 y 3 letras
texto = frase_res.split()
palabras_2_y_3_letras = [palabra for palabra in texto if len(palabra) in (2, 3)]
print("")
print("palabras con 2 y 3 letras")
print(palabras_2_y_3_letras)
print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)


#De aqui "22 AX JIvCXPQKX AX 1936" suponesmos que pone "22 de noviembre de 1936"

#sabiendo que la A=d
print ("Sustituimos la letra A por la d")
texto_modificado = frase_res.replace('A', 'd')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'd', 'A')

claves_lista_ord.remove('A')
L_max_prob.remove('d')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)


#sabiendo que la X=e 
print ("Sustituimos la letra X por la e")
texto_modificado = frase_res.replace('X', 'e')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'e', 'X')

claves_lista_ord.remove('X')
L_max_prob.remove('e')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)


#sabiendo que la J=n
print ("Sustituimos la letra J por la n")
texto_modificado = frase_res.replace('J', 'n')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'n', 'J')

claves_lista_ord.remove('J')
L_max_prob.remove('n')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#sabiendo que la I=o
print ("Sustituimos la letra I por la o")
texto_modificado = frase_res.replace('I', 'o')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'o', 'I')

claves_lista_ord.remove('I')
L_max_prob.remove('o')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#sabiendo que la C=i
print ("Sustituimos la letra C por la i")
texto_modificado = frase_res.replace('C', 'i')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'i', 'C')

claves_lista_ord.remove('C')
L_max_prob.remove('i')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#sabiendo que la P=m
print ("Sustituimos la letra P por la m")
texto_modificado = frase_res.replace('P', 'm')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'm', 'P')

claves_lista_ord.remove('P')
L_max_prob.remove('m')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#sabiendo que la Q=b
print ("Sustituimos la letra Q por la b")
texto_modificado = frase_res.replace('Q', 'b')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'b', 'Q')

claves_lista_ord.remove('Q')
L_max_prob.remove('b')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#sabiendo que la K=r
print ("Sustituimos la letra K por la r")
texto_modificado = frase_res.replace('K', 'r')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'r', 'K')

claves_lista_ord.remove('K')
L_max_prob.remove('r')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

# Con esta palabra "revoTZRionErio" podemos seguir completando "revolucionario"

#sabiendo que la T=l
print ("Sustituimos la letra T por la l")
texto_modificado = frase_res.replace('T', 'l')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'l', 'T')

claves_lista_ord.remove('T')
L_max_prob.remove('l')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#sabiendo que la Z=u
print ("Sustituimos la letra Z por la u")
texto_modificado = frase_res.replace('Z', 'u')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'u', 'Z')

claves_lista_ord.remove('Z')
L_max_prob.remove('u')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#sabiendo que la R=c
print ("Sustituimos la letra R por la c")
texto_modificado = frase_res.replace('R', 'c')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'c', 'R')

claves_lista_ord.remove('R')
L_max_prob.remove('c')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#sabiendo que la E=a
print ("Sustituimos la letra E por la a")
texto_modificado = frase_res.replace('E', 'a')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'a', 'E')

claves_lista_ord.remove('E')
L_max_prob.remove('a')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)


# De "Hradicion" sabemos que es "Tradicion"
#sabiendo que la H=t
print ("Sustituimos la letra H por la t")
texto_modificado = frase_res.replace('H', 't')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 't', 'H')

claves_lista_ord.remove('H')
L_max_prob.remove('t')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

# De "claNe obrera" sabemos que es "clase obrera"
#sabiendo que la N=s
print ("Sustituimos la letra N por la s")
texto_modificado = frase_res.replace('N', 's')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 's', 'N')

claves_lista_ord.remove('N')
L_max_prob.remove('s')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)


#Vamos a ver que letras faltan por descifrar
print("")
print(claves_lista_ord)
print("")
print(L_max_prob)
print("")
print(Solucion_claves)



#Con "diriUente"  que es "dirigente"
#sabiendo que la U=g
print ("Sustituimos la letra U por la g")
texto_modificado = frase_res.replace('U', 'g')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'g', 'U')

claves_lista_ord.remove('U')
L_max_prob.remove('g')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)



#Con "Oascismo"  que es "fascismo"
#sabiendo que la O=f
print ("Sustituimos la letra O por la f")
texto_modificado = frase_res.replace('O', 'f')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'f', 'O')

claves_lista_ord.remove('O')
L_max_prob.remove('f')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)



#Con "indeDendencia"  que es "independencia"
#sabiendo que la D=p
print ("Sustituimos la letra D por la p")
texto_modificado = frase_res.replace('D', 'p')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'p', 'D')

claves_lista_ord.remove('D')
L_max_prob.remove('p')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)



#Con "anarSuista"  que es "anarquista"
#sabiendo que la S=q
print ("Sustituimos la letra S por la q")
texto_modificado = frase_res.replace('S', 'q')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'q', 'S')

claves_lista_ord.remove('S')
L_max_prob.remove('q')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)


#Volvemos a ver que letras faltan por descifrar
print("")
print(claves_lista_ord)
print("")
print(L_max_prob)
print("")
print(Solucion_claves)



#Con "meGor eFpresaba "  que es "mejor expresaba "
#sabiendo que la G=j
print ("Sustituimos la letra G por la j")
texto_modificado = frase_res.replace('G', 'j')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'j', 'G')

claves_lista_ord.remove('G')
L_max_prob.remove('j')

#sabiendo que la F=x
print ("Sustituimos la letra F por la x")
texto_modificado = frase_res.replace('F', 'x')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'x', 'F')

claves_lista_ord.remove('F')
L_max_prob.remove('x')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)

#Volvemos a ver que letras faltan por descifrar
print("")
print(claves_lista_ord)
print("")
print(L_max_prob)
print("")
print(Solucion_claves)

#En las listas vemos que coincide la V con la y, y viendo catalunVa tiene sentido el cambio a catalunya
#sabiendo que la V=y
print ("Sustituimos la letra V por la y")
texto_modificado = frase_res.replace('V', 'y')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'y', 'V')

claves_lista_ord.remove('V')
L_max_prob.remove('y')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)


# Mistoria -> Historia
#sabiendo que la M=h
print ("Sustituimos la letra M por la h")
texto_modificado = frase_res.replace('M', 'h')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'h', 'M')

claves_lista_ord.remove('M')
L_max_prob.remove('h')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)


#Volvemos a ver que letras faltan por descifrar
print("")
print(claves_lista_ord)
print("")
print(L_max_prob)
print("")
print(Solucion_claves)

# desmoraliLando -> desmoralizando
#sabiendo que la L=z
print ("Sustituimos la letra L por la z")
texto_modificado = frase_res.replace('L', 'z')
frase_res = texto_modificado
Solucion_claves = agregar_elemento(Solucion_claves, 'z', 'L')

claves_lista_ord.remove('L')
L_max_prob.remove('z')

print("")
print("Como va quedando la frase paso " + str(x))
x += 1
print(frase_res)



#Volvemos a ver que letras faltan por descifrar
print("")
print(claves_lista_ord)
print("")
print(L_max_prob)
print("")
print(Solucion_claves)

# Por ultimo nos faltaria sustituir la v por su correspondiente pero vemos que equivale a lo mismo, pero aun asi lo añadimos a la lista de claves
#La v = v
claves_lista_ord.remove('v')
L_max_prob.remove('v')

#Resultado final
print("")
print("")
print("***************** SOLUCION *****************")
print("")
print("El texto cifrado es: ")
print("")
print(frase)
print("")
print("La lista de claves para descifrarlo es: ")
print("")
print(Solucion_claves)
print("")
print("El texto descrifrado es: ")
print(frase_res)