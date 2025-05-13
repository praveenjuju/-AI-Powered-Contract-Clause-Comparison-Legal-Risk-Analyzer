import fitz  # PyMuPDF
import docx

def extract_clauses_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.split("\n\n")

def extract_clauses_from_docx(file):
    doc = docx.Document(file)
    text = [para.text for para in doc.paragraphs if para.text.strip() != ""]
    return text
