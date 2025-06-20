# LLM PDF Parser

This project uses OpenAI's GPT-4 to intelligently extract specific fields from a PDF document. The fields to extract are configurable via a `config.json` file, and the output is returned in JSON format.

## 📄 Features

- 🔍 Extracts user-defined fields from text-based PDFs.
- 🤖 Uses OpenAI GPT-4 to parse and understand document structure.
- ⚙️ Configurable fields for flexible use across documents.
- 📤 Outputs clean JSON data for further processing.

## 🧰 Requirements

- Python 3.7+
- Packages:
  - openai
  - PyMuPDF (`fitz`)
  - (Optional) pytesseract and Pillow for OCR fallback

Install required packages:

```bash
pip install openai PyMuPDF
```

## 🗂️ Project Structure

```
llm_pdf_parser/
├── main.py         # Main script to extract fields using GPT-4
├── config.json     # List of fields to extract
```

## ⚙️ Configuration

Update `config.json` with fields you want to extract from the PDF:

```json
{
  "fields_to_extract": [
    "Invoice Number",
    "Invoice Date",
    "Customer Name",
    "Total Amount",
    "Due Date"
  ]
}
```

## 🚀 How to Use

1. Place the PDF file in the same directory and update its name in `main.py`.
2. Run the script:

```bash
python main.py
```

3. The result will be printed as a JSON object with field-value pairs.

## 🔐 Environment

Make sure to set your OpenAI API key:

```bash
export OPENAI_API_KEY=your_api_key_here
```

## 📦 Future Enhancements

- OCR fallback for scanned PDFs
- Streamlit UI
- Batch processing
- Schema validation

## 🧠 Powered By

- [OpenAI GPT-4](https://platform.openai.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)

---

Feel free to fork, contribute, and suggest enhancements!