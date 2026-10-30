import pymupdf
from pathlib import Path
from app.ingestion.text_cleaner import clean_text

def load_pdf(file_path: str) -> list[dict]:
    pdf_path = Path(file_path)
    if not pdf_path.exists():
        raise FileNotFoundError(file_path)

    with pymupdf.open(pdf_path) as pdf:

        documents = []
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text")
            text = clean_text(text)
            if not text:
                continue

            documents.append({
                "text": text,
                "metadata": {
                    "source": pdf_path.name,
                    "page": page_number,
                    "total_pages": pdf.page_count
                } 
            })

    return documents