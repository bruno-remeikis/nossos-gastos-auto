from docling.document_converter import DocumentConverter

from markdown_reader import MarkdownReader

print("Carregando arquivo...")

source = "./itau_extrato_032025.pdf"

converter = DocumentConverter()
result = converter.convert(source)
markdown = result.document.export_to_markdown()

print("Processando dados...")

reader = MarkdownReader(markdown)
reader.goto("##")
reader.goto_list()
reader.prune_tail("##")

reader.print()

#for i in range(40):
while True:
    row = reader.get_row_as_array()
    if row == None:
        break
    print(row)