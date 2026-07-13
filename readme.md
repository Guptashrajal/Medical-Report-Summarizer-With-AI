# 🏥 Medical Report Summarizer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg)](https://streamlit.io)

> AI-powered medical report summarization using RAG (Retrieval-Augmented Generation) with LangChain and Streamlit.

---

## ✨ Features

- 📄 Upload PDF, DOCX, TXT medical reports
- 🤖 AI-powered summaries with key information extraction
- 💬 Ask questions about your reports
- 🔒 Privacy-first: local processing available
- 🎨 Clean, intuitive interface

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/siddharthcode-24/Medical-Report-Summarizer.git
cd Medical-Report-Summarizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 📖 Usage

1. **Upload** medical reports (PDF/DOCX/TXT)
2. **Process** documents to create embeddings
3. **Generate** comprehensive summary
4. **Ask** questions about the reports

### Example Queries
- "What medications are prescribed?"
- "Summarize the lab results"
- "List all diagnoses"

---

## 📁 Project Structure

```
├── app.py              # Main app
├── src/                # Core logic
├── data/               # Vector store
└── requirements.txt    # Dependencies
```

---

## ⚙️ Configuration

Edit `.env` file:

```env
OPENAI_API_KEY=your-api-key-here
MODEL_NAME=gpt-3.5-turbo
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

---

## 📋 Requirements

```txt
streamlit>=1.28.0
langchain>=0.1.0
langchain-openai>=0.0.5
faiss-cpu>=1.7.4
pypdf2>=3.0.0
python-docx>=1.1.0
python-dotenv>=1.0.0
tiktoken>=0.5.1
```

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
## Output
<img width="934" height="535" alt="Screenshot 2025-10-12 194356" src="https://github.com/user-attachments/assets/9696c8b9-b9a1-4565-88af-f6c8f2a1d982" />
<img width="1322" height="762" alt="Screenshot 2025-10-12 194327" src="https://github.com/user-attachments/assets/f9bc44dd-ffc8-4c69-9eb2-05a0c63f0f77" />
<img width="1254" height="700" alt="Screenshot 2025-10-12 194346" src="https://github.com/user-attachments/assets/4189bd79-332a-4fe4-bb5b-a41014858768" />







## ⚠️ Disclaimer

This tool assists healthcare professionals but should not replace clinical judgment. Always verify AI-generated summaries.

---

## 📞 Contact

- GitHub:siddharthcode-24
- Email: siddharthbajaj24@gmail.com

---

<div align="center">

**Made with ❤️ for healthcare professionals**

⭐ Star this repo if you find it helpful!

</div>
