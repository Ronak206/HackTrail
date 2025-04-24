import re
from utils.pdf_reader import extract_pdf_text
from utils.preprocessing import preprocess

class CVParserAgent:
    def extract_info(self, text):
        name = re.search(r"Name:\s*(.*)", text)
        email = re.search(r"Email:\s*([^\s]+)", text)
        phone = re.search(r"Phone:\s*([^\s]+)", text)
        return (
            name.group(1).strip() if name else "Not Found",
            email.group(1).strip() if email else "Not Found",
            phone.group(1).strip() if phone else "Not Found"
        )

    def parse(self, file_path):
        raw_text = extract_pdf_text(file_path)
        clean_text = preprocess(raw_text)
        name, email, phone = self.extract_info(raw_text)
        return {
            "filename": file_path,
            "raw_text": raw_text,
            "clean_text": clean_text,
            
            "name": name,
            "email": email,
            "phone": phone
        }