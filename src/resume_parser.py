# resume_parser.py - Module for parsing resumes

import pdfplumber


def extract_text_from_pdf(pdf_file):

    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""
    return text.strip()

# Example usage
if __name__ == "__main__":
    # Test the function with a sample PDF (replace 'sample_resume.pdf' with an actual file path)
    pdf_path = "Resume_Airbus.pdf"
    with open(pdf_path, "rb") as pdf_file:
        resume_text = extract_text_from_pdf(pdf_file)
        print("Extracted Resume Text:")
        print(resume_text)
