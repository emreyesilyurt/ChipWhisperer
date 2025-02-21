
import fitz  # PyMuPDF

def classify_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    for page in doc:
        text = page.get_text()
        if text.strip():
            return "text"
    return "image"
