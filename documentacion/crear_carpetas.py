import os
import json

def crear_carpetas(inicio: int = 1, fin: int = 170, prefijo: str = "clase_") -> None:
    """
    Crea carpetas con nombres consecutivos tipo 'clase_001' hasta 'clase_170'
    y dentro de cada carpeta un archivo vacío 'notas.json'.

    Args:
        inicio (int): Número inicial.
        fin (int): Número final.
        prefijo (str): Prefijo del nombre de la carpeta.
    """
    for i in range(inicio, fin + 1):
        nombre = f"{prefijo}{i:03d}"  # clase_001, clase_002, ...
        os.makedirs(nombre, exist_ok=True)

        # Ruta al archivo notas.json dentro de la carpeta
        ruta_json = os.path.join(nombre, "notas.json")

        # Crear archivo vacío (si no existe ya)
        if not os.path.exists(ruta_json):
            with open(ruta_json, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=4)  # archivo vacío con {}
        
        print(f"Carpeta creada: {nombre} | Archivo: {ruta_json}")

if __name__ == "__main__":
    crear_carpetas()
