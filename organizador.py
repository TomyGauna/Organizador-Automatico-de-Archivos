import os
import shutil
import argparse

# Diccionario de tipos de archivo por categoría
TIPOS_ARCHIVOS = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Música": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Instaladores": [".exe", ".msi", ".dmg", ".apk"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"]
}


def obtener_categoria(extension):
    for categoria, extensiones in TIPOS_ARCHIVOS.items():
        if extension.lower() in extensiones:
            return categoria
    return "Otros"


def mover_archivo(ruta_origen, destino_base, categoria, nombre_archivo):
    destino_categoria = os.path.join(destino_base, categoria)
    if not os.path.exists(destino_categoria):
        os.makedirs(destino_categoria)
        print(f"[+] Carpeta creada: {categoria}")
    else:
        print(f"[*] Carpeta ya existente: {categoria}")

    destino_archivo = os.path.join(destino_categoria, nombre_archivo)

    # Si ya existe un archivo con ese nombre, crear uno nuevo
    if os.path.exists(destino_archivo):
        nombre_base, extension = os.path.splitext(nombre_archivo)
        contador = 1
        while os.path.exists(destino_archivo):
            nuevo_nombre = f"{nombre_base}_copia{contador}{extension}"
            destino_archivo = os.path.join(destino_categoria, nuevo_nombre)
            contador += 1

    shutil.move(ruta_origen, destino_archivo)
    print(f"    → {nombre_archivo} movido a '{categoria}'")


def organizar_archivos(carpeta):
    total_organizados = 0
    total_desconocidos = 0

    for nombre_archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, nombre_archivo)

        if os.path.isfile(ruta_completa):
            _, extension = os.path.splitext(nombre_archivo)
            categoria = obtener_categoria(extension)

            mover_archivo(ruta_completa, carpeta, categoria, nombre_archivo)

            total_organizados += 1 if categoria != "Otros" else 0
            total_desconocidos += 1 if categoria == "Otros" else 0

    print("\n✅ Organización completada.")
    print(f"   Archivos organizados: {total_organizados}")
    print(f"   Archivos sin categoría: {total_desconocidos}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organizador de archivos por tipo")
    parser.add_argument("--carpeta", type=str, help="Ruta de la carpeta a organizar")
    args = parser.parse_args()

    if args.carpeta:
        carpeta = args.carpeta
    else:
        carpeta = input("Por favor ingrese la carpeta que desea organizar: ")

    if not os.path.exists(carpeta):
        print(f"❌ La carpeta '{carpeta}' no existe.")
        exit()

    organizar_archivos(carpeta)
