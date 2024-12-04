 # Purpose: Extracts complete form field data from a PDF, including labels.
# Usage: python extract_form_fields_4.py
# Example PDF: f966.pdf
# Example Output: form966_fields.json
# Note: This script requires the PyMuPDF library, which can be installed via pip.
# Note: This script is intended to be used with the provided example PDF.
import json
import fitz

def extract_form_field_data(pdf_path):
    """Extracts complete form field data from a PDF, including labels."""

    doc = fitz.open(pdf_path)
    form_fields = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for field in page.widgets():
            field_data = {
                "name": field.field_name,
                "type": field.field_type,
                "rect": [field.rect.x0, field.rect.y0, field.rect.x1, field.rect.y1],
                "options": field.field_flags,
                "label": "",  # Initialize label as empty
                "value": "",
            }

            # Try to find the label by searching nearby text blocks

            for block in page.get_text("dict")["blocks"]:
                if block["type"] == 0:  # Text block
                    for line in block["lines"]:
                        for span in line["spans"]:
                            if field.rect.contains(span["bbox"]):
                                field_data["label"] = span["text"].strip()
                                break  # Found a potential label

            form_fields.append(field_data)

    return form_fields

def save_to_json(data, output_path):
    """Saves data to a JSON file."""

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    pdf_path = "f966.pdf"
    output_json_path = "form966_fields.json"

    form_field_data = extract_form_field_data(pdf_path)
    save_to_json(form_field_data, output_json_path)

    print(f"Form field data saved to: {output_json_path}")