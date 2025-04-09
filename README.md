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
✅ **Configurable Processing** - Uses a configuration file to manage LLM model selections and parameters.  
✅ **Logging & Pre/Post Processing** - Keeps logs and allows additional text cleanup.  
✅ **Command-line Interface** - Easy to use from the command line with various options.

---

## 🏗 Project Structure
```
ChipWhisperer/
│── src/
│   ├── main.py                        # Entry point with CLI interface
│   ├── vllm_pdf_extractor.py          # Core extraction logic (GPT-4V & Llama 3)
│── utils/
│   ├── helper.py                      # General helper functions
│   ├── logger.py                      # Logging utilities
│   ├── pdf_reader.py                  # PDF classification and metadata
│── classifier/
│   ├── model.py                       # Placeholder for future ML-based classifiers
│   ├── preprocessor.py                # Preprocessing for PDFs
│   ├── postprocessor.py               # Post-processing extracted text
│── tests/
│   ├── test_vllm_pdf_extractor.py     # Unit tests for extraction logic
│   ├── test_pdf_reader.py             # Unit tests for PDF classification
│── configs/
│   ├── config.json                    # Configuration settings
│── logs/                              # Directory for log files
│── examples/
│   ├── sample.pdf                     # Example PDFs
│── requirements.txt                   # Dependencies
├── README.md                          # Project documentation
```

---

## 🛠 Installation

### **🔹 Prerequisites**
Ensure you have:
- **Python 3.8+**
- **Ollama installed** (for Llama 3) - https://ollama.com/
- **OpenAI API Key** (for GPT-4V access)

### **🔹 Install Dependencies**
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/emreyesilyurt/chipwhisperer.git
cd chipwhisperer
pip install -r requirements.txt
```

### **🔹 Set Up Environment Variables**
```bash
# Set your OpenAI API key (required for GPT-4V)
export OPENAI_API_KEY=your_openai_api_key

# Make sure Ollama is running (for Llama 3)
# Default URL: http://localhost:11434
```

---

## 🚀 Usage

### **🔹 Basic Usage**
To process a PDF with automatic detection:

```bash
python src/main.py --pdf path/to/your/document.pdf
```

### **🔹 Command-line Options**
```bash
# Process a PDF and save the output to a file
python src/main.py --pdf input.pdf --output results.txt

# Force using GPT-4V regardless of PDF type
python src/main.py --pdf input.pdf --force-vllm

# Force using Llama 3 regardless of PDF type
python src/main.py --pdf input.pdf --force-llama
```

### **🔹 Running Tests**
Run the unit tests:

```bash
python -m unittest discover tests
```

---

## ⚙️ Configuration

You can customize the tool's behavior by modifying `configs/config.json`:

```json
{
    "vllm_model": "gpt-4-vision-preview",
    "llama3_model": "llama3",
    "extraction": {
        "image_quality": 2,
        "max_tokens": 4096,
        "chunk_size": 32000,
        "temperature": 0.0
    },
    "classification": {
        "text_threshold": 50,
        "text_page_ratio": 0.5
    },
    "ollama": {
        "api_url": "http://localhost:11434/api/chat"
    },
    "processing": {
        "clean_text": true,
        "extract_sections": false,
        "section_headings": [
            "Abstract",
            "Introduction",
            "Background",
            "Methods",
            "Results",
            "Discussion",
            "Conclusion",
            "References"
        ]
    }
}
```

---

## 🎯 Future Improvements
- **Fine-tuned models** for specific document types
- **Layout recognition** for complex PDF structures (tables, multi-columns)
- **Enhanced section detection** for academic papers
- **Batch processing** for handling multiple PDFs
- **API interface** for integration with other applications
- **Web interface** for easier use

---

## 📜 License
MIT License - See LICENSE file for details.

## 🔗 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
