from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("img.png")

ws.add_image(img, "C3") # C3 위치에 img.png 파일 이미지 삽임

wb.save("sample_image.xlsx")