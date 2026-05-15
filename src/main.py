from pathlib import Path
from PIL import Image
import pytesseract
import pandas as pd

# Conexión con Tesseract en Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
RESULTS_DIR = BASE_DIR / "results" / "ocr_outputs"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Extensiones permitidas para la lectura de datos
valid_extensions = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]

results = []

for image_path in RAW_DIR.iterdir():
    if image_path.suffix not in valid_extensions:
        continue

    print(f"Procesando imagen: {image_path.name}")

    try:
        image = Image.open(image_path)

        extracted_text = pytesseract.image_to_string(image, lang="spa")

        output_txt = RESULTS_DIR / f"{image_path.stem}_tesseract.txt"

        with open(output_txt, "w", encoding="utf-8") as file:
            file.write(extracted_text)

        results.append({
            "file_name": image_path.name,
            "ocr_engine": "Tesseract OCR",
            "output_file": output_txt.name,
            "extracted_text": extracted_text
        })

    except Exception as e:
        print(f"Error procesando {image_path.name}: {e}")

# Guardar resumen general
df_results = pd.DataFrame(results)
df_results.to_csv(BASE_DIR / "results" / "ocr_results_tesseract.csv", index=False, encoding="utf-8-sig")

print("\nProceso finalizado.")
print(f"Imágenes procesadas: {len(results)}")
print(f"Resultados guardados en: {RESULTS_DIR}")
print(f"Archivo resumen: results/ocr_results_tesseract.csv")