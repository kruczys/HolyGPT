import fitz

pdf_path = 'PS.pdf'
txt_path = 'bible_pol_unclean.txt'

pdf_document = fitz.open(pdf_path)

with open(txt_path, 'w', encoding="utf-8") as file:
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text = page.get_text()
        file.write(text)
        file.write('\n\n')

print('Text extracted from PDF and saved to', txt_path)
