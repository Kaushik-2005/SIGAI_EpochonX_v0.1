import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

class DocxGenerator:
    def __init__(self):
        self.document = Document()

    def generate(self, report_content: str, filename: str = "progress_report.docx"):
        # Split the content by lines and process each line
        lines = report_content.split('\n')
        
        for line in lines:
            # Check for different sections to format properly
            if line.strip().upper() == line.strip() and len(line.strip()) > 0:  # Assuming uppercase lines are headings
                self.add_heading(line.strip())
            elif line.endswith(":"):  # Assuming lines ending with ":" are member names or section titles
                self.add_bold_text(line.strip())
            elif line.startswith("- ") or line.startswith("• "):  # Assuming lines starting with "-" or "•" are bulleted lists
                self.add_bullet_point(line.strip()[2:])
            else:
                self.add_normal_text(line.strip())

        # Save the document
        try:
            # Get the absolute path of the current working directory
            current_dir = os.path.abspath(os.getcwd())
            file_path = os.path.join(current_dir, filename)
            
            self.document.save(file_path)
            print(f"Report saved successfully as: {file_path}")
        except Exception as e:
            print(f"Error saving the document: {str(e)}")
            print(f"Attempted to save at: {file_path}")

    def add_heading(self, text: str):
        """Adds a bold heading to the document."""
        p = self.document.add_paragraph()
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(14)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def add_bold_text(self, text: str):
        """Adds bold text to the document for member names or section titles."""
        p = self.document.add_paragraph()
        p.add_run(text).bold = True

    def add_bullet_point(self, text: str):
        """Adds a bullet point to the document."""
        self.document.add_paragraph(text, style='List Bullet')

    def add_normal_text(self, text: str):
        """Adds normal text to the document."""
        self.document.add_paragraph(text)
