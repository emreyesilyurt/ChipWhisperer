
# ChipWhisperer PDF Extractor (GPT-4V + Llama 3)

## 📌 Overview
ChipWhisperer is a **hybrid PDF text extraction tool** that intelligently determines whether a PDF is **image-based or text-based** and applies the most suitable **Large Language Model (LLM)** to extract meaningful content.

### 🔹 **How it Works**
- If the PDF **contains selectable text**, the tool **uses Llama 3** (via Ollama) to extract and summarize the text.
- If the PDF is **scanned (image-based)**, the tool **uses GPT-4V** (GPT-4 Vision) to **intelligently extract** the text.

This approach ensures **higher accuracy** compared to traditional OCR while leveraging **LLM capabilities** to improve text structuring.

---

## 🚀 Features
✅ **Automated PDF Classification** - Detects whether a PDF is text-based or image-based.  
✅ **GPT-4V for Image-Based PDFs** - Extracts text from scanned or image-based documents.  
✅ **Llama 3 for Text-Based PDFs** - Extracts and summarizes content from PDFs with selectable text.  
✅ **Modular Structure** - Supports easy modifications and enhancements.  
✅ **Configurable Processing** - Uses a configuration file to manage LLM model selections.  
✅ **Logging & Pre/Post Processing** - Keeps logs and allows additional text cleanup.  

---

## 🏗 Project Structure
```
ChipWhisperer_vLLM_GPT4V_Llama3/
│── src/
│   ├── main.py                        # Entry point for text extraction
│   ├── vllm_pdf_extractor.py          # GPT-4V for images, Llama 3 for text PDFs
│── utils/
│   ├── helper.py                       # General helper functions
│   ├── logger.py                       # Logging utilities
│   ├── pdf_reader.py                   # PDF classification (image/text)
│── classifier/
│   ├── model.py                         # Placeholder for future ML-based classifiers
│   ├── preprocessor.py                  # Preprocessing for PDFs
│   ├── postprocessor.py                 # Post-processing extracted text
│── tests/
│   ├── test_vllm_pdf_extractor.py      # Unit tests for extraction logic
│   ├── test_pdf_reader.py              # Unit tests for PDF classification
│── configs/
│   ├── config.json                     # Configuration settings (GPT-4V & Llama 3)
│── examples/
│   ├── sample.pdf                      # Placeholder for sample PDFs
│── requirements.txt                     # Dependencies
├── README.md                       # Project documentation
```

---

## 🛠 Installation

### **🔹 Prerequisites**
Ensure you have:
- **Python 3.8+**
- **Ollama installed** (for Llama 3)
- **OpenAI API Key** (for GPT-4V access)

### **🔹 Install Dependencies**
Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### **🔹 Running the Extraction Pipeline**
To process a PDF and extract text:

```bash
python src/main.py
```

This will determine whether the PDF is **text-based or image-based** and apply the appropriate model.

### **🔹 Running Tests**
Run unit tests to verify functionality:

```bash
python -m unittest discover tests
```

---

## ⚙️ Configuration

You can configure model settings inside `configs/config.json`:

```json
{
    "vllm_model": "gpt-4-vision-preview",
    "llama3_model": "llama3"
}
```

This allows **future improvements** by switching models easily.

---

## 🎯 Future Improvements
The project is designed to **scale** and support additional capabilities, such as:
- **Fine-tuned models for specific document types.**
- **Improved layout understanding for complex PDFs (e.g., tables, multi-columns).**
- **Additional pre/post-processing for better text structuring.**

---

## 🤖 LLM Integration for Future Enhancements
This README serves as a reference **for future LLM-based improvements** by providing:
- **Clear definitions** of how the system works.
- **Structured code breakdown** to help LLMs generate enhancements.
- **A step-by-step guide** for future developers.

This setup makes **future modifications easier**, whether by AI-assisted programming or manual improvements.

---

## 📜 License
MIT License - Feel free to modify and improve!

