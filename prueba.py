import os

extensiones = [
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".mp3", ".wav", ".aac", ".flac", ".mp4", ".mkv", ".mov", ".avi", ".exe", ".msi", ".dmg", ".apk", ".zip", ".rar", ".7z", ".tar", ".gz", "", ".a"
]

# Nombre de la carpeta
nombre_carpeta = "carpeta_de_prueba"

# Crear la carpeta si no existe
if not os.path.exists(nombre_carpeta):
    os.makedirs(nombre_carpeta)


# Crear los archivos dentro de la carpeta
for ext in extensiones:
    ruta_archivo = os.path.join(nombre_carpeta, f"a{ext}")
    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, "wb") as f:
            f.write(b"")  # Archivo vacío
    else:
        print(f"✖ Ya existe: {ruta_archivo}")
