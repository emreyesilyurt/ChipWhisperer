# ChipWhisperer: LLM-Based Product Notification Classifier  

ChipWhisperer is an AI-powered classification system designed to **automate the categorization of Product Change Notifications (PCN) and Product Discontinuation Notifications (PDN)** in the electronics industry. By leveraging **LLaMA 3**, served via **Ollama**, this solution streamlines notification processing, reducing manual effort and improving accuracy.  

## 🔹 Key Features  
- **Automated PCN/PDN Classification** – Uses LLaMA 3 to intelligently categorize product notifications.  
- **Efficient Model Serving** – Powered by **Ollama** for optimized inference.  
- **Scalable & High-Performance** – Processes large volumes of documents with minimal latency.  
- **Enhanced Accuracy** – Reduces human intervention, improving consistency in decision-making.  

## 🚀 How It Works  
1. **Ingestion** – ChipWhisperer extracts and preprocesses product notifications.  
2. **Classification** – The LLaMA 3 model predicts and categorizes PCN/PDN notifications.  
3. **Serving** – Ollama efficiently serves the model, ensuring smooth and fast execution.  
4. **Output** – The results are structured for downstream applications.  

## 🛠️ Installation & Setup  
### Prerequisites  
- Python 3.8+  
- Ollama installed and configured  
- Dependencies from `requirements.txt`  

### Steps  
```sh
git clone https://github.com/your-repo/ChipWhisperer.git  
cd ChipWhisperer  
pip install -r requirements.txt  
python main.py  
```

## 📌 Use Case  
ChipWhisperer is ideal for **electronic component distributors, manufacturers, and supply chain analysts** who need to process large volumes of product notifications efficiently.

## 🤝 Contributing  
We welcome contributions! Feel free to submit issues and pull requests.

## 📜 License  
This project is licensed under [MIT License](LICENSE).
