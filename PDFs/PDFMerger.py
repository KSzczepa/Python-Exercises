import PyPDF2
import sys

inputs = sys.argv[1:]
watermark_pdf = 'wtr.pdf'
merged_pdf = 'merged.pdf'
merged_with_watM = 'mergedWaterm.pdf'


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(merged_pdf)


def pdf_add_watermark(pdf_file, watermarked_file):
    with open(pdf_file, 'rb') as input_file, open(watermark_pdf, 'rb') as watermark_file:
        input_pdf = PyPDF2.PdfFileReader(input_file)
        watermark = PyPDF2.PdfFileReader(watermark_file)
        watermark_page = watermark.getPage(0)

        output = PyPDF2.PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            pdf_page = input_pdf.getPage(i)
            pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)

        with open(watermarked_file, 'wb') as merged_file:
            output.write(merged_file)


pdf_combiner(inputs)
pdf_add_watermark(merged_pdf, merged_with_watM)
