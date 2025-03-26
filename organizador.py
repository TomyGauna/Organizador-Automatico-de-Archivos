import os

tipos_archivos = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Musica": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Instaladores": [".exe", ".msi", ".dmg", ".apk"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"]
}


carpeta = input("por favor ingre la carpeta que desa organizar: ")

if not carpeta.endswith("\\"):
    carpeta += "\\"

# Recorremos los archivps dentro de la carpeta
for nombre_archivo in os.listdir(carpeta):
    ruta_completa = os.path.join(carpeta, nombre_archivo)

    # Verificamos que sea un archivo (no una subcarpeta)
    if os.path.isfile(ruta_completa):
        _, extension = os.path.splitext(nombre_archivo)
        print(f"{nombre_archivo} -> {extension}")
        for categoria, extensiones in tipos_archivos.items():
            if extension.lower() in extensiones:
                print(f"Este archivo es un {categoria}")
                break
            if not os.path.exists(carpeta + categoria):
                # Crear la carpeta si no existe
                os.makedirs(carpeta + categoria)
                print(f"La carpeta '{categoria}' ha sido creada.")
            else:
                print(f"La carpeta '{categoria}' ya existe.")
        else:
            print("Categoría desconocida")