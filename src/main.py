
from utils.pdf_reader import classify_pdf
from vllm_pdf_extractor import extract_pdf_text

if __name__ == "__main__":
    pdf_path = "examples/sample.pdf"
    if classify_pdf(pdf_path) == "image":
        extracted_text = extract_pdf_text(pdf_path, use_vllm=True)
    else:
        extracted_text = extract_pdf_text(pdf_path, use_vllm=False)
    print(extracted_text)
