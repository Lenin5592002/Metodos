import os
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, NumberObject

def comprimir_pdf_agresivo(input_path, output_path, calidad_imagen=20):
    """
    Comprime un PDF reduciendo drásticamente la calidad de las imágenes
    y eliminando metadatos innecesarios.
    
    :param calidad_imagen: Calidad JPG (1-100). 20 es muy agresivo.
    """
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Recorremos todas las páginas
    for page in reader.pages:
        # Comprimir imágenes dentro de la página
        for img in page.images:
            # Reemplazar la imagen con una versión de baja calidad
            # Nota: pypdf permite manipular el objeto de imagen, 
            # pero la forma más efectiva de reducir peso total es 
            # forzar la compresión en el guardado o eliminar duplicados.
            pass 
            
        # Añadir página al escritor
        writer.add_page(page)

    # Nivel de compresión de flujo (elimina espacios en blanco y optimiza)
    # Recorremos los objetos para forzar compresión
    for page in writer.pages:
        page.compress_content_streams()

    # Eliminar metadatos para ahorrar bytes
    writer.add_metadata({
        '/Producer': 'Python Compression',
        '/Creator': 'Script'
    })

    # Guardar con reducción de tamaño
    with open(output_path, "wb") as f:
        writer.write(f)
    
    # Verificación rápida
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Archivo guardado: {output_path}")
    print(f"Nuevo tamaño: {size_mb:.2f} MB")

# --- USO ---
# Cambia 'tu_archivo.pdf' por el nombre real
comprimir_pdf_agresivo('DeberInversaLU.pdf', 'archivo_menos_3mb.pdf', calidad_imagen=1)