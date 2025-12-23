import pdfplumber

def extract_text_from_pdf(pdf_path, output_txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n\n"
    
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Text extracted to {output_txt_path}")

if __name__ == "__main__":
    extract_text_from_pdf("casestudies.pdf", "extracted_text.txt")
