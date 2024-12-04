# Fill the f966.pdf form using data from the JSON file.
# Usage: python fill_f966_from_json_7.py
# Example PDF: f966.pdf
# Example JSON: f966_fields.json
# Example Output: filled_form966.pdf
# Note: This script requires the PyMuPDF library, which can be installed via pip.
# Note: This script is intended to be used with the provided example PDF and JSON.

import fitz
import json

def fill_f966_form(pdf_path, data_json_path, output_pdf_path):
    """Fills the f966.pdf form using data from the JSON file."""

    with open(data_json_path, "r", encoding="utf-8") as f:
        form_field_data = json.load(f)

    doc = fitz.open(pdf_path)

    for field_data in form_field_data:
        label = field_data["label"]
        value = field_data["value"]

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            for field in page.widgets():
                if field.field_name == field_data["name"]:
                    value = field_data["value"]
                    
                    #handle checkboxes
                    #will only get checked if value in JSON file is true
                    if field.field_type == 2:
                        field.field_value = value
                              # Mark checkbox as unchecked

                    # Handle text fields (field_type == 7)
                    elif field.field_type == 7 or field.field_type == 1:  # Text field
                        field.field_value = value
                          # Ensure the field gets updated
                         # Ensure the checkbox gets updated
                    
                    # Handle radio boxes (field_type == 5)
                    #in order to fill them in, the JSON file would need to have the proper
                    #label for each radio box
                    elif field.field_type == 5:
                        #if field.on_state()
                        #print(field.field_value)
                        if value:
                            field.field_value = field.on_state()
                            #print(f"Radio button '{field.field_name}' on_state: {field.on_state()} {field.field_value}" )
                        #if field.on_state == "Choice1":
                        
                        
                    
                    field.update()  # Ensure the checkbox gets updated
                    

                    '''
                    if field.field_type == 7:  # Text field
                        annot = page.first_annot
                        while annot:
                            if annot.xref == field.xref:
                                page.delete_annot(annot)
                                break
                            annot = annot.next

                        # Create and insert the new text field (adjusted position)
                        page.insert_text(
                            (field.rect.x0 + 5, field.rect.y0 + 10),  # Adjusted offset and margin
                            value,
                            fontsize=field.text_fontsize
                        )
                    elif field.field_type == 2:  # Checkbox
                        field.field_value = int(value)
                        if field.field_value == 1:
                            page.draw_rect(field.rect, color=field.border_color, width=field.border_width)
                            x0, y0, x1, y1 = field.rect.x0, field.rect.y0, field.rect.x1, field.rect.y1
        # Draw the first diagonal line
                            page.draw_line((x0, y0), (x1, y1), color=(0, 0, 0), width=1)  # Black line
                            
                            # Draw the second diagonal line
                            page.draw_line((x0, y1), (x1, y0), color=(0, 0, 0), width=1) 
                                            

                    # ... Handle other field types as needed ...

  '''
                                           

                    # ... Handle other field types as needed ...

    doc.save(output_pdf_path)
    print(f"Form filled and saved to: {output_pdf_path}")

if __name__ == "__main__":
    pdf_path = "f966.pdf"
    data_json_path = "prompt_4.json"
    output_pdf_path = "filled_form_966_label4.pdf"

    fill_f966_form(pdf_path, data_json_path, output_pdf_path)