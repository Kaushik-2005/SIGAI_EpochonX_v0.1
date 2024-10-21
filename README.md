# DocxGenerator with Progress Report Bot

This project combines a DocxGenerator for creating formatted Word documents and a Progress Report Generator bot that uses AI to create structured progress reports.

## Features:
- **DocxGenerator:** 
  - Markdown-like Formatting: Supports headings, bold text, italic text, and list items.
  - Word Document Generation: Converts formatted plain text into a structured .docx file.
  - Cross-drive Compatibility: Handles file saving across different drives.
  - Error Handling: Provides fallback to temporary files in case of permission issues.
- **Progress Report Bot:**
  - AI-Powered Report Generation: Uses Google's Generative AI to create detailed progress reports.
  - User Input Collection: Gathers report details through an interactive command-line interface.
  - Flexible Output: Generates reports based on user input or test data.
  - Integration with DocxGenerator: Saves the generated report as a formatted Word document.

## Requirements:
- Python 3.6+
- python-docx
- langchain
- google-generativeai
- python-dotenv

## Structure:
```bash
.
├── document_generator.py  # Contains the DocxGenerator class
├── bot.py                 # Contains the ProgressReportGenerator class
├── requirements.txt       # Contains the required dependencies
└── README.md              # Project documentation
```

## Installation:
1. Clone the repository:
```bash
git clone https://github.com/Kaushik-2005/SIGAI_EpochonX_v0.1.git
cd SIGAI_EpochonX_v0.1
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Google API key in a `.env` file:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage:
### DocxGenerator
```python
from document_generator import DocxGenerator

doc_generator = DocxGenerator()
doc_generator.generate("# My Report\n\nThis is a **sample** report.", "my_report.docx")
```

### Progress Report Bot
```python
from bot import ProgressReportGenerator

generator = ProgressReportGenerator()

# Using test inputs
test_inputs = generator.get_test_input()
report = generator.generate_and_save_report(test_inputs)

# Using user inputs
user_inputs = generator.get_user_input()
report = generator.generate_and_save_report(user_inputs, "user_progress_report.docx")
```

## Detailed Component Descriptions:

### bot.py (ProgressReportGenerator)

The `bot.py` file contains the `ProgressReportGenerator` class, which is responsible for generating AI-powered progress reports. Key features include:

1. **AI Integration:** Uses Google's Generative AI (Gemini 1.5 Pro) via the `langchain` library to generate report content.
2. **Customizable Prompt:** Utilizes a detailed prompt template to guide the AI in creating structured reports.
3. **User Input Collection:** Provides an interactive CLI to gather detailed information about the report period, team members, and their contributions.
4. **Test Data Generation:** Includes a method to generate sample data for quick testing and demonstration.
5. **Report Generation and Saving:** Combines AI-generated content with the DocxGenerator to create and save formatted Word documents.

Key methods:
- `get_user_input()`: Collects detailed report information from the user.
- `get_test_input()`: Provides sample data for testing.
- `generate_report(inputs)`: Uses AI to generate the report content.
- `generate_and_save_report(inputs, filename)`: Generates the report and saves it as a Word document.

### document_generator.py (DocxGenerator)

The `document_generator.py` file contains the `DocxGenerator` class, which is responsible for creating formatted Word documents. Key features include:

1. **Markdown-like Parsing:** Interprets basic markdown syntax for formatting text.
2. **Document Structuring:** Creates properly formatted Word documents with headings, bold text, and normal paragraphs.
3. **Cross-platform Compatibility:** Uses temporary files and shutil to ensure compatibility across different drives and operating systems.
4. **Error Handling:** Provides informative error messages and fallback options if saving fails.

Key methods:
- `generate(report_content, filename)`: Main method to create and save the Word document.
- `add_heading(text)`: Adds a formatted heading to the document.
- `add_bold_text(text)`: Adds bold text to the document.
- `add_normal_text(text)`: Adds normal paragraph text to the document.

## Supported Formatting:
The DocxGenerator supports the following markdown-like syntax:
- Headings: Start a line with `#`
- Bold: Surround text with `*` or `_`
- Italic: Surround text with single `*` or `_`
- List items: Start a line with `-`, `+`, or a number

## Contributing:
Contributions to improve this project are welcome. Please feel free to submit a Pull Request.

## License:
[Specify your chosen license here]

## Contact:
[Your contact information or where to report issues]