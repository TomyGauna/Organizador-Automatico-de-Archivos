import os
import shutil
import argparse
import customtkinter as ctk
from tkinter import filedialog, messagebox

# 💼 Configuración visual
ctk.set_appearance_mode("dark")  # "light", "dark", "system"
ctk.set_default_color_theme("dark-blue")

# 📦 Tipos de archivo
TIPOS_ARCHIVOS = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Música": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Instaladores": [".exe", ".msi", ".dmg", ".apk"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

# 📂 Clasificación
def obtener_categoria(extension):
    for categoria, extensiones in TIPOS_ARCHIVOS.items():
        if extension.lower() in extensiones:
            return categoria
    return "Otros"

# 📁 Movimiento de archivo
def mover_archivo(ruta_origen, destino_base, categoria, nombre_archivo):
    destino_categoria = os.path.join(destino_base, categoria)
    if not os.path.exists(destino_categoria):
        os.makedirs(destino_categoria)

    destino_archivo = os.path.join(destino_categoria, nombre_archivo)

    # Evita sobrescribir si ya existe
    if os.path.exists(destino_archivo):
        nombre_base, extension = os.path.splitext(nombre_archivo)
        contador = 1
        while os.path.exists(destino_archivo):
            nuevo_nombre = f"{nombre_base}_copia{contador}{extension}"
            destino_archivo = os.path.join(destino_categoria, nuevo_nombre)
            contador += 1

    shutil.move(ruta_origen, destino_archivo)

# ⚙ Función principal
def organizar_archivos(carpeta):
    total_organizados = 0
    total_desconocidos = 0

    for nombre_archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, nombre_archivo)

        if os.path.isfile(ruta_completa):
            _, extension = os.path.splitext(nombre_archivo)
            categoria = obtener_categoria(extension)

            mover_archivo(ruta_completa, carpeta, categoria, nombre_archivo)

            if categoria == "Otros":
                total_desconocidos += 1
            else:
                total_organizados += 1

    return total_organizados, total_desconocidos

# 🖥️ Interfaz gráfica
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organizador de Archivos")
        self.geometry("500x300")
        self.resizable(False, False)

        self.label_titulo = ctk.CTkLabel(self, text="Organizador automático de archivos", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_titulo.pack(pady=(30, 10))

        self.boton = ctk.CTkButton(self, text="Seleccionar carpeta", command=self.seleccionar_carpeta, width=200, height=40, font=ctk.CTkFont(size=14))
        self.boton.pack(pady=10)

        self.resultado = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14), justify="center", wraplength=400)
        self.resultado.pack(pady=20)

    def seleccionar_carpeta(self):
        carpeta = filedialog.askdirectory(title="Seleccionar carpeta a organizar")
        if carpeta:
            total, otros = organizar_archivos(carpeta)
            mensaje = f"✔ Organización completa.\n\nArchivos organizados: {total}\nSin categoría: {otros}"
            self.resultado.configure(text=mensaje)
            messagebox.showinfo("Organización completada", "La carpeta ha sido organizada con éxito.")

# Entrada principal: CLI o GUI
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organizador de archivos por tipo")
    parser.add_argument("--modo", choices=["gui", "cli"], help="Modo de ejecución: gui o cli")
    parser.add_argument("--carpeta", type=str, help="Ruta de la carpeta a organizar (solo en modo cli)")
    args = parser.parse_args()

    # 👉 Si se pasó --carpeta, asumimos modo cli
    if args.carpeta and not args.modo:
        args.modo = "cli"
    elif not args.modo:
        args.modo = "gui"

    if args.modo == "cli":
        carpeta = args.carpeta or input("Por favor ingrese la carpeta que desea organizar: ")

        if not os.path.exists(carpeta):
            print(f"❌ La carpeta '{carpeta}' no existe.")
            exit()

        total, otros = organizar_archivos(carpeta)
        print(f"\n✅ Organización completada.\nArchivos organizados: {total}\nSin categoría: {otros}")
    else:
        app = App()
        app.mainloop()
