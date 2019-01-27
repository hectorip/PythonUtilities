import PyPDF2
import os

def get_filename(name, source):
    return os.path.join(source, name)

def concatenate(name1, name2, skip_pages=0, dst_file='final.pdf', source='sources'):
    wf = open(get_filename(dst_file, source), 'ab')
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
