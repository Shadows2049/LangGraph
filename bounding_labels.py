# Purpose: Extract form field data from a PDF, draw bounding boxes with UUIDs for automated labeling, and save form field data with UUIDs to a JSON file.
# Usage: python bounding_labels.py
# Example PDF: f966.pdf
# Example Output PDF: labeled_form966.pdf
# Example Output JSON: f66_fields.json
# Note: This script requires the PyMuPDF library, which can be installed via pip.
# Note: This script is intended to be used with the provided example PDF.
import fitz
import json
import uuid

def process_pdf_form(pdf_path, output_pdf_path, output_json_path):
    """
    1. Extracts form field data.
    2. Draws bounding boxes with UUIDs for manual labeling.
    3. Saves form field data with UUIDs to a JSON file.
    """

    doc = fitz.open(pdf_path)
    form_field_data = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for field in page.widgets():
            unique_id = str(uuid.uuid4())
            field_data = {
                "uuid": unique_id,
                "name": field.field_name,
                "type": field.field_type,
                "rect": [field.rect.x0, field.rect.y0, field.rect.x1, field.rect.y1],
                "options": field.field_flags,
                "label": "",  # You can manually fill this in later
                "value": ""
            }
            form_field_data.append(field_data)

            # Draw bounding box and UUID on the PDF
            page.draw_rect(field.rect, color=(1, 0, 0), width=1) 
            page.insert_text(
                (field.rect.x0+1, field.rect.y1 - 2),
                unique_id,
                fontsize=6,
                color=(1, 0, 0)
            )

    doc.save(output_pdf_path)

    # Save form field data with UUIDs to JSON
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(form_field_data, f, indent=4)

    print(f"Bounding boxes drawn and saved to: {output_pdf_path}")
    print(f"Form field data with UUIDs saved to: {output_json_path}")
    
"""   custom_date_field = {
        "uuid": str(uuid.uuid4()),  # Generate a custom UUID
        "name": "custom_field_date",  # Custom field name
        "type": 7,  # Assuming it's a text field (type 7)
        "rect": [468.0, 432.0000305175781, 669.6, 444.0010070800781],  # Adjust the bounding box as needed
        "options": 8388608,  # Field options (adjust as needed)
        "label": "Date",  # Assign a custom label
        "value": ""  # Value can be filled in later or left empty
    }
"""
if __name__ == "__main__":
    pdf_path = "f966-f.pdf"
    output_pdf_path = "labeled_f966.pdf"
    output_json_path = "form966_fields.json"
    process_pdf_form(pdf_path, output_pdf_path, output_json_path)