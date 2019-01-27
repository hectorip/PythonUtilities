import PyPDF2
import os

def get_filename(source, name):
    return os.path.join(name, source)

def get_pages(name, pages = [], source='sources'):
    complete_name = get_filename(name, source)
    with open(complete_name, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        print(pdf_reader.numPages)
        pdf_pages = []
        pages = pages or range(pdf_reader.numPages)
        for p in pages:
            pdf_pages.append(pdf_reader.getPage(p))
        return pdf_pages

# pdfReader1 = open_pdf('Chapter1.pdf')
# print(pdfReader1.numPages)

def concatenate(name1, name2, source='sources'):
    pdf1_pages = get_pages(name1)
    pdf2_pages = get_pages(name2)
    return pdf1_pages + pdf2_pages
    # print('total %s' % (len(pdf1_pages) + len(pdf2_pages)))


with open("dst/final.pdf", 'wb') as wf:
    pdfw = PyPDF2.PdfFileWriter()
    pages = concatenate("Chapter1.pdf", "Chapter2.pdf")
    for p in pages:
        pdfw.addPage(p)
    pdfw.write(wf)