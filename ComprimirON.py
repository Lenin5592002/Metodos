import fitz  # Se importa como 'fitz' aunque instalaste 'pymupdf'
import os

def aplanar_y_comprimir(input_path, output_path):
    print(f"Abriendo: {input_path}...")
    
    try:
        doc = fitz.open(input_path)
        new_doc = fitz.open() # Aquí crearemos el PDF nuevo
        
        for i, page in enumerate(doc):
            # 1. 'Fotografiamos' la página (Rasterizar)
            # matrix=fitz.Matrix(0.5, 0.5) reduce la resolución a la mitad (Zoom 50%)
            # Esto baja el peso DRAMÁTICAMENTE.
            pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5)) 
            
            # 2. Convertimos esa 'foto' a datos JPG comprimidos
            # jpg_quality=20 es baja calidad (muy agresivo)
            img_bytes = pix.tobytes("jpg", jpg_quality=70)
            
            # 3. Creamos una página nueva en el PDF destino con esa foto
            new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
            new_page.insert_image(new_page.rect, stream=img_bytes)
            
            print(f"Procesando página {i+1}...")

        # Guardamos el resultado
        new_doc.save(output_path)
        
        # Verificamos peso final
        size_mb = os.path.getsize(output_path) / (1376 * 1376)
        print(f"\n¡Listo! Archivo guardado en: {output_path}")
        print(f"Nuevo tamaño: {size_mb:.2f} MB")
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# --- TUS RUTAS ---
# RECUERDA: Usa la 'r' antes de las comillas y pega la ruta que copiaste antes
input_pdf = r"C:\Users\Lenin\Desktop\Workspace2025\Talleres\Evaluaciones\DeberInversaLU.pdf"
output_pdf = r"C:\Users\Lenin\Desktop\Workspace2025\Talleres\Evaluaciones\Deber_Comprimido_OneNote.pdf"

aplanar_y_comprimir(input_pdf, output_pdf)