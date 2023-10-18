import os
from PIL import Image
import hashlib
import numpy  as np


hash_conocido = "e5ed313192776744b9b93b1320b5e268"
es_imagen = False

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = "/home/eneko/Documentos/Universidad/Seguridad/Lab_1/imagen/"

# Obtener una lista de nombres de archivo en la carpeta
archivos = os.listdir(carpeta_imagenes)

# Inicializar un índice para recorrer la lista de archivos
indice = 0

while indice < len(archivos) and not es_imagen:
    nombre_archivo = archivos[indice]

    # Verificar si el archivo es una imagen (por ejemplo, con extensión .jpg)
    if nombre_archivo.lower().endswith((".jpg")):
        ruta_completa = os.path.join(carpeta_imagenes, nombre_archivo)
        
        # Leer la imagen utilizando Pillow
        imagen = Image.open(ruta_completa)

        #
        with open(ruta_completa, "rb") as file:
            contenido_imagen = file.read()
            hash_calculado = hashlib.md5(contenido_imagen).hexdigest()
    
        # Compara el hash calculado con el hash conocido
        if hash_calculado == hash_conocido:
            print("Es la imagen que buscabamos")
            es_imagen = True
            ruta_buscada = ruta_completa
            contenido_buscado = contenido_imagen
            hash_buscado = hash_calculado

        else:
            print("Esta imagen no es")
            # Incrementar el índice
            indice += 1
    else:
        # Si no es una imagen, pasa al siguiente archivo
        indice += 1


print("")
print("Ruta buscada: ")
print(ruta_buscada)
print("")
print("Contenifo bucado: ")
#print(contenido_buscado)
print("")
print("Hash buscado: ")
print(hash_buscado)


print("")
print("Sabiendo que es la imagen 22, la introducimos en stegosuite y la extraemos, teniendo como resutlado la siguiente frase: Al Fascismo no se le discute, se le destruye. Buenaventura Durruti")