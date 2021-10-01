import PyPDF2

with open('dummy.pdf', 'rb') as file:    #rb - read binary
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)              #return num of pages

    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

