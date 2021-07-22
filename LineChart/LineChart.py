from datetime import date
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.axis import DateAxis

wb = Workbook ()
ws = wb.active

rows = [
    ['Date', 'Batch 1', 'Batch2', 'Batch3'],
    [date(2015,9, 1), 10, 30, 25],
    [date(2015,9, 2), 20, 25, 30],
    [date(2015,9, 3), 30, 30, 45],
    [date(2015,9, 4), 40, 25, 40],
    [date(2015,9, 5), 55, 35, 30],
    [date(2015,9, 6), 60, 40, 35],
]

for row in rows:
    ws.append(row)

c1 = LineChart()
c1.title = "Line Chart"
c1.legend = None
c1.style = 15
c1.y_axis.title = 'Size'
c1.x_axis.title = 'Test Number'

data = Reference(ws, min_col=2, min_row=1, max_col=4, max_row=7)
c1.add_data(data, titles_from_data=True)

ws.add_chart(c1, "A10")

wb.save("line.xlsx")