from docx import Document

def read_table(doc_path):
    document = Document(doc_path)

    # Assuming there's only one table in the document
    table = document.tables[0]

    data = {}
    for col_idx, col in enumerate(table.columns):
        col_data = [cell.text for cell in col.cells]
        data[f'Column_{col_idx + 1}'] = col_data

    return data

# Replace 'your_document.docx' with the actual path to your Word document
document_path = 'your_document.docx'
table_data = read_table(document_path)

for column, values in table_data.items():
    print(f'{column}: {values}')
