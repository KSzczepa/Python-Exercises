from openpyxl import Workbook
from openpyxl.drawing.image import Image


wb = Workbook()
ws = wb.active

img = Image('cat.jpg')
img2 = Image('shark.jpg')
img2.anchor = 'P4'
ws.add_image(img, 'A1')
ws.add_image(img2)

wb.save('cat.xlsx')