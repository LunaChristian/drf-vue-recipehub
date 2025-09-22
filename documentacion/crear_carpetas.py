import os

def crear_dialogos(inicio: int = 12, fin: int = 170, prefijo: str = "clase_") -> None:
    """
    Crea un archivo 'dialogo.txt' en cada carpeta desde 'clase_12' hasta 'clase_170'.
    No modifica ni crea otros archivos.
    """
    for i in range(inicio, fin + 1):
        nombre_carpeta = f"{prefijo}{i}"  # clase_12, clase_13, ...
        
        if os.path.exists(nombre_carpeta) and os.path.isdir(nombre_carpeta):
            ruta_txt = os.path.join(nombre_carpeta, "dialogo.txt")
            
            # Crear el archivo solo si no existe
            if not os.path.exists(ruta_txt):
                with open(ruta_txt, "w", encoding="utf-8") as f:
                    f.write("")  # archivo vacío
                print(f"Archivo creado: {ruta_txt}")
            else:
                print(f"Ya existía: {ruta_txt}")
        else:
            print(f"No existe la carpeta: {nombre_carpeta}")

if __name__ == "__main__":
    crear_dialogos()
