from llm_pdf_parser.parser import extract_text_from_pdf
from llm_pdf_parser.config_loader import load_fields
from llm_pdf_parser.llm_client import build_prompt, query_llm
import json

def parse_pdf(pdf_path, config_path):
    text = extract_text_from_pdf(pdf_path)
    fields = load_fields(config_path)
    prompt = build_prompt(text, fields)
    response = query_llm(prompt)
    try:
        return json.loads(response)
    except:
        return {"error": "Failed to parse response", "raw": response}

if __name__ == "__main__":
    result = parse_pdf("examples/sample_invoice.pdf", "config.json")
    print(json.dumps(result, indent=2))