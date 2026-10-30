from app.ingestion.pdf_loader import load_pdf
from pathlib import Path


path_pdf = Path("data/pdfs/sample.pdf")

documents = load_pdf(path_pdf)
print("Total pages extracted: ", len(documents))

for document in documents:
    extracted_text = document["text"]
    print(extracted_text)
    print(document["metadata"])