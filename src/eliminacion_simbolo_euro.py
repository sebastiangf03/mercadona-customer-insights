# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:20:47 2024

@author: pablo
"""

import os

def quitar_simbolo_euro(carpeta):
    """
    Esta función quita el símbolo del euro (€) de todos los nombres de archivos en una carpeta especificada.

    :param carpeta: Ruta de la carpeta donde se encuentran los archivos.
    """
    try:
        # Lista todos los archivos en la carpeta
        archivos = os.listdir(carpeta)

        for archivo in archivos:
            # Verifica si el nombre del archivo contiene el símbolo del euro
            if '€' in archivo:
                # Genera el nuevo nombre del archivo
                nuevo_nombre = archivo.replace('€', '')

                # Obtiene las rutas completas del archivo original y el nuevo archivo
                ruta_original = os.path.join(carpeta, archivo)
                ruta_nueva = os.path.join(carpeta, nuevo_nombre)

                # Renombra el archivo
                os.rename(ruta_original, ruta_nueva)
                print(f"Renombrado: {archivo} -> {nuevo_nombre}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
carpeta = "data/"
quitar_simbolo_euro(carpeta)
