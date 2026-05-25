from pathlib import Path
import shutil

# carpeta a organizar
carpeta = Path.home() / "Downloads"

tipos_archivos = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Programas": [".exe", ".msi"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Musica": [".mp3", ".wav"]
}

for archivo in carpeta.iterdir():

    if archivo.is_dir():
        continue

    # obtiene extensión
    extension = archivo.suffix.lower()

    for carpeta_destino, extensiones in tipos_archivos.items():

        if extension in extensiones:

            # crea carpeta si no existe
            destino = carpeta / carpeta_destino
            destino.mkdir(exist_ok=True)

            # mueve archivo
            shutil.move(str(archivo), str(destino / archivo.name))

            print(f"Movido: {archivo.name} → {carpeta_destino}")

            break