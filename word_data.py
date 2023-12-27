from docx import Document

def read_table(doc_path):
    document = Document(doc_path)

    # Assuming there's only one table in the document
    table = document.tables[0]

    data = []
    for row in table.rows:
        row_data = [cell.text for cell in row.cells]
        data.append(row_data)

    return data

# Replace 'your_document.docx' with the actual path to your Word document
document_path = 'your_document.docx'
table_data = read_table(document_path)

for row in table_data:
    print(row)
