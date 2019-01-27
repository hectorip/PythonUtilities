import PyPDF2
import os

def get_filename(name, source):
    return os.path.join(source, name)

def concatenate(name1, name2, skip_pages=0, source='sources'):
    wf = open(get_filename('final.pdf', source), 'ab')
    with open(get_filename(name1, source), 'rb') as rf1:
        with open(get_filename(name2, source), 'rb') as rf2:
            pdf1 = PyPDF2.PdfFileReader(rf1)
            pdf2 = PyPDF2.PdfFileReader(rf2)
            writer = PyPDF2.PdfFileWriter()
            for p in range(pdf1.numPages):
                writer.addPage(pdf1.getPage(p))

            for p in range(skip_pages, pdf2.numPages):
                writer.addPage(pdf2.getPage(p))
            writer.write(wf)
            wf.close()
    # print('total %s' % (len(pdf1_pages) + len(pdf2_pages)))



chapters = ["Chapter{}.pdf".format(n) for n in range(3,12)]
# final_file = "final.pdf"
# create_pdf(final_file)
concatenate("Chapter1.pdf", "Chapter2.pdf", 2)
for chapter in chapters:
    concatenate("final.pdf", chapter, 2)
