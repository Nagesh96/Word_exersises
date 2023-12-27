from docx import Document

def read_table(doc_path):
    document = Document(doc_path)

    # Assuming there's only one table in the document
    table = document.tables[0]

    data = {}
    for row in table.rows[1:]:  # Skip the header row
        student_name = row.cells[1].text.strip()
        marks = int(row.cells[2].text.strip())
        data[student_name] = marks

    return data

# Replace 'your_document.docx' with the actual path to your Word document
document_path = 'your_document.docx'
table_data = read_table(document_path)

for student, marks in table_data.items():
    print(f'{student}: {marks}')
