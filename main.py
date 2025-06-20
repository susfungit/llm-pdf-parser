from llm_pdf_parser.parser import extract_text_streaming
from llm_pdf_parser.config_loader import load_fields
from llm_pdf_parser.llm_client import build_prompt, query_llm
import json

def parse_pdf(pdf_path, config_path):
    fields = load_fields(config_path)
    combined_text = ""

    for page_num, text in extract_text_streaming(pdf_path, keywords=None, max_pages=20):
        combined_text += f"\n--- Page {page_num} ---\n{text}\n"

    prompt = build_prompt(combined_text, fields)
    response = query_llm(prompt)
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {"error": "Failed to parse response", "raw": response}

if __name__ == "__main__":
    result = parse_pdf("examples/sample_invoice.pdf", "config.json")
    print(json.dumps(result, indent=2))