
import fitz  # PyMuPDF
import openai

def extract_pdf_text(pdf_path, use_vllm=True):
    if use_vllm:
        return extract_text_with_gpt4v(pdf_path)
    else:
        return extract_text_with_llama3(pdf_path)

def extract_text_with_gpt4v(pdf_path):
    """Use GPT-4V to extract text from image-based PDFs."""
    doc = fitz.open(pdf_path)
    extracted_text = ""
    
    for page_num, page in enumerate(doc):
        pix = page.get_pixmap()
        image_data = pix.tobytes("png")  # Convert page to PNG format

        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[{"role": "user", "content": "Extract text from this document page."}],
            files=[{"mime_type": "image/png", "data": image_data}]
        )

        extracted_text += response["choices"][0]["message"]["content"] + "\n"
    
    return extracted_text

def extract_text_with_llama3(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = "\n".join([page.get_text("text") for page in doc])
    
    response = openai.ChatCompletion.create(
        model="llama3",
        messages=[{"role": "user", "content": f"Summarize the following PDF text:\n{full_text}"}]
    )
    return response["choices"][0]["message"]["content"]
