from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader, PdfMerger
import math

print("Welcome to PCS-Diagram generator")
min_number = 0
max_number = 11
user_input = input("Enter your pitch-class set, using integers separated by commas (e.g. '0,4,7,9'): ")
#user_input = "10,11,2,3,4"
numbers = [int(num.strip()) for num in user_input.split(',') if min_number <= int(num) <= max_number]
numbers.sort()
polygonColor = input("Set the color of your set ('red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey' or 'none'): ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("courier", "", 16)

pdf.set_line_width(0.5)

#SET YOUR COLORS HERE
circleColor = (0, 0, 0)
indexesColor = circleColor
textColor = circleColor #Set to (255, 255, 255) for invisible labels
# polygonColor = "red"

#CIRCLE PARAMETERS (do not modify)
xCircle = 50
yCircle = 50
dCircle = 70

rCircle = dCircle/2
xCenterCircle = xCircle + rCircle
yCenterCircle = yCircle + rCircle

pdf.set_draw_color(circleColor)
pdf.circle(x=xCircle, y=yCircle, r=dCircle, style="D")

#LENGTH OF THE INDEXES (do not modify)
indexLength = 2
halfIndexLength = indexLength/2

#DRAW LABELS (do not modify)
pdf.set_text_color(textColor)
x0 = x6 = 83.4
x1 = x5 = 103
x2 = x4 = 118
x3 = 122
x9 = 44
y0 = 46.8
y1 = y11 = 52.3
y2 = y10 = 68
y3 = y9 = 86.5
y4 = y8 = 106
y5 = y7 = 121
y6 = 126.5
x7= x11 = 63
x8 = x10 = 49

pdf.text(x0, y0, "0")
pdf.text(103, y1, "1")
pdf.text(x2, y2, "2")
pdf.text(x3, y3, "3")
pdf.text(x4, y4, "4")
pdf.text(x5, y5, "5")
pdf.text(x6, y6, "6")
pdf.text(x7, y7, "7")
pdf.text(x8, y8, "8")
pdf.text(x9, y9, "9")
pdf.text(x10, y10, "t")
pdf.text(x11, y11, "e")

#DRAW INDEXES (do not modify)
#3H
pdf.set_draw_color(indexesColor)
pdf.line(x1=xCenterCircle + rCircle - halfIndexLength, 
         y1=yCenterCircle, 
         x2=xCenterCircle + rCircle + halfIndexLength, 
         y2=yCenterCircle)

#6H
pdf.line(x1=xCenterCircle, 
         y1=yCenterCircle + rCircle - halfIndexLength,
         x2=xCenterCircle, 
         y2=yCenterCircle + rCircle + halfIndexLength,)

#9H
pdf.line(x1=xCenterCircle - rCircle - halfIndexLength, 
         y1=yCenterCircle, 
         x2=xCenterCircle - rCircle + halfIndexLength, 
         y2=yCenterCircle)

#12H
pdf.line(x1=xCenterCircle, 
         y1=yCenterCircle - rCircle - halfIndexLength, 
         x2=xCenterCircle, 
         y2=yCenterCircle - rCircle + halfIndexLength)

#1H
pdf.line(x1=xCenterCircle + rCircle * math.cos(math.pi/3) + halfIndexLength * math.cos(2*math.pi/3), 
         y1=yCenterCircle - rCircle * math.sin(math.pi/3) + halfIndexLength * math.sin(2*math.pi/3), 
         x2=xCenterCircle + rCircle * math.cos(math.pi/3) - halfIndexLength * math.cos(2*math.pi/3), 
         y2=yCenterCircle - rCircle * math.sin(math.pi/3) - halfIndexLength * math.sin(2*math.pi/3))

#2H
pdf.line(x1=xCenterCircle + rCircle * math.cos(math.pi/6) - halfIndexLength * math.cos(5*math.pi/6), 
         y1=yCenterCircle - rCircle * math.sin(math.pi/6) - halfIndexLength * math.sin(5*math.pi/6), 
         x2=xCenterCircle + rCircle * math.cos(math.pi/6) + halfIndexLength * math.cos(5*math.pi/6), 
         y2=yCenterCircle - rCircle * math.sin(math.pi/6) + halfIndexLength * math.sin(5*math.pi/6))

#4H
pdf.line(x1=xCenterCircle + rCircle * math.cos(math.pi/6) - halfIndexLength * math.cos(math.pi/6), 
         y1=yCenterCircle + rCircle * math.sin(math.pi/6) - halfIndexLength * math.sin(math.pi/6), 
         x2=xCenterCircle + rCircle * math.cos(math.pi/6) + halfIndexLength * math.cos(math.pi/6), 
         y2=yCenterCircle + rCircle * math.sin(math.pi/6) + halfIndexLength * math.sin(math.pi/6))

#5H
pdf.line(x1=xCenterCircle + rCircle * math.cos(math.pi/3) + halfIndexLength * math.cos(math.pi/3), 
         y1=yCenterCircle + rCircle * math.sin(math.pi/3) + halfIndexLength * math.sin(math.pi/3), 
         x2=xCenterCircle + rCircle * math.cos(math.pi/3) - halfIndexLength * math.cos(math.pi/3), 
         y2=yCenterCircle + rCircle * math.sin(math.pi/3) - halfIndexLength * math.sin(math.pi/3))

#7H
pdf.line(x1=xCenterCircle - rCircle * math.cos(math.pi/3) + halfIndexLength * math.cos(2*math.pi/3), 
         y1=yCenterCircle + rCircle * math.sin(math.pi/3) + halfIndexLength * math.sin(2*math.pi/3), 
         x2=xCenterCircle - rCircle * math.cos(math.pi/3) - halfIndexLength * math.cos(2*math.pi/3), 
         y2=yCenterCircle + rCircle * math.sin(math.pi/3) - halfIndexLength * math.sin(2*math.pi/3))

#8H
pdf.line(x1=xCenterCircle - rCircle * math.cos(math.pi/6) - halfIndexLength * math.cos(5*math.pi/6), 
         y1=yCenterCircle + rCircle * math.sin(math.pi/6) - halfIndexLength * math.sin(5*math.pi/6), 
         x2=xCenterCircle - rCircle * math.cos(math.pi/6) + halfIndexLength * math.cos(5*math.pi/6), 
         y2=yCenterCircle + rCircle * math.sin(math.pi/6) + halfIndexLength * math.sin(5*math.pi/6))

#10H
pdf.line(x1=xCenterCircle - rCircle * math.cos(math.pi/6) - halfIndexLength * math.cos(math.pi/6), 
         y1=yCenterCircle - rCircle * math.sin(math.pi/6) - halfIndexLength * math.sin(math.pi/6), 
         x2=xCenterCircle - rCircle * math.cos(math.pi/6) + halfIndexLength * math.cos(math.pi/6), 
         y2=yCenterCircle - rCircle * math.sin(math.pi/6) + halfIndexLength * math.sin(math.pi/6))

#11H
pdf.line(x1=xCenterCircle - rCircle * math.cos(math.pi/3) - halfIndexLength * math.cos(math.pi/3), 
         y1=yCenterCircle - rCircle * math.sin(math.pi/3) - halfIndexLength * math.sin(math.pi/3), 
         x2=xCenterCircle - rCircle * math.cos(math.pi/3) + halfIndexLength * math.cos(math.pi/3), 
         y2=yCenterCircle - rCircle * math.sin(math.pi/3) + halfIndexLength * math.sin(math.pi/3))

#COORDINATES (do not modify)
coordOf = [(xCenterCircle, yCenterCircle - rCircle), #0
           (xCenterCircle + rCircle * math.cos(math.pi/3), yCenterCircle - rCircle * math.sin(math.pi/3)), #1
           (xCenterCircle + rCircle * math.cos(math.pi/6), yCenterCircle - rCircle * math.sin(math.pi/6)), #2
           (xCenterCircle + rCircle, yCenterCircle), #3
           (xCenterCircle + rCircle * math.cos(math.pi/6), yCenterCircle + rCircle * math.sin(math.pi/6)), #4
           (xCenterCircle + rCircle * math.cos(math.pi/3), yCenterCircle + rCircle * math.sin(math.pi/3)), #5
           (xCenterCircle, yCenterCircle + rCircle), #6
           (xCenterCircle - rCircle * math.cos(math.pi/3), yCenterCircle + rCircle * math.sin(math.pi/3)), #7
           (xCenterCircle - rCircle * math.cos(math.pi/6), yCenterCircle + rCircle * math.sin(math.pi/6)), #8
           (xCenterCircle - rCircle, yCenterCircle), #9
           (xCenterCircle - rCircle * math.cos(math.pi/6), yCenterCircle - rCircle * math.sin(math.pi/6)), #10
           (xCenterCircle - rCircle * math.cos(math.pi/3), yCenterCircle - rCircle * math.sin(math.pi/3))] #11

#DRAW SET
polygonStyle = "DF"

if polygonColor == "orange":
    colorDraw = (182, 108, 32)
    colorFill = (247, 206 , 156)

elif polygonColor == "blue":
    colorDraw = (103, 139, 193)
    colorFill = (216, 231, 253)

elif polygonColor == "green":
    colorDraw = (108, 186, 102)
    colorFill = (207, 235, 212)

elif polygonColor == "grey":
    colorDraw = (110)
    colorFill = (227)

elif polygonColor == "red":
    colorDraw = (219, 91, 91)
    colorFill = (255, 203, 202)

elif polygonColor == "yellow":
    colorDraw = (204, 169, 69)
    colorFill = (255, 239, 193)

elif polygonColor == "violet":
    colorDraw = (132, 92, 150)
    colorFill = (218, 202, 226)

elif polygonColor == "none":
    colorDraw = (0, 0, 0)
    colorFill = (0, 0, 0)
    polygonStyle = "D"

pdf.set_draw_color(colorDraw)
pdf.set_fill_color(colorFill)

coords = [coordOf[num] for num in numbers]  

if 2 < len(coords) < 13: 
    pdf.polygon(coords, style=polygonStyle)

pdf.output("/tmp/circle.pdf")

#CROP PDF
with open("/tmp/circle.pdf", "rb") as in_f:
    input1 = PdfReader(in_f)
    output = PdfWriter()

    page = input1.pages[0]

    page.cropbox.lower_left = (120, 475)
    page.cropbox.upper_right = (360, 725)
    output.add_page(page)

with open("pcset_circle.pdf", "wb") as out_f:
    output.write(out_f)
