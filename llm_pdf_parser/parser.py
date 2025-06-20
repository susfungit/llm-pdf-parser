import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import logging

logging.basicConfig(level=logging.INFO)

def extract_text_from_image_page(page):
    pix = page.get_pixmap(dpi=300)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return pytesseract.image_to_string(img)

def extract_text_streaming(file_path, keywords=None, max_pages=None):
    """
    Extracts text page-by-page from a PDF.
    Uses OCR for image-based pages.

    Args:
        file_path (str): Path to the PDF file.
        keywords (list of str): If provided, only extract pages containing these keywords.
        max_pages (int): Max number of pages to process.

    Returns:
        generator of (page_number, text)
    """
    doc = fitz.open(file_path)
    for i, page in enumerate(doc):
        if max_pages and i >= max_pages:
            break

        text = page.get_text().strip()
        if not text:
            logging.info(f"Page {i+1} has no text, using OCR...")
            text = extract_text_from_image_page(page)

        if keywords:
            if any(keyword.lower() in text.lower() for keyword in keywords):
                yield (i + 1, text)
        else:
            yield (i + 1, text)
