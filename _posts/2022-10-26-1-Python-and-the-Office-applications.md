---
layout: post
tag: Microsoft Office, VBA, python, automation
category: "education"
title: "Python and the Office applications"
description: Use VBA in Python and the other way too
author: Sarah Chen
image: images/posts/office.PNG
---

- [Introduction](#introduction)
- [Excel](#excel)
- [Outlook](#outlook)
- [PowerPoint](#powerpoint)
  - [Create dashboard](#create-dashboard)
  - [Copy from Excel to PowerPoint](#copy-from-excel-to-powerpoint)
- [Run VBA code from Python](#run-vba-code-from-python)

# Introduction
Most of the corporate office work is still immersed in MS Office: Excel, Outlook emails, PowerPoint and Word documents.  To reduce Office fatigue, we can use Python.  

The <span class="coding">win32com</span> library enables use and publish our own COM (Component Object Model) objects without having to understand the details of how the object was created or implemented.
In addition to <span class="coding">win32com</span>, the <span class="coding">openpyxl</span> library and <span class="coding">pptx</span>, as their names imply, help us create and modify Excel and PowerPoint files. 

# Excel

Below is an example of how we start an Excel instance by win32com.client.Dispatch("Excel.Application").  
By default object is not visible unless we set the Visible property to True.  You can call the object anything you like, for example, just <span class="coding">E</span>  to get away from Office. 

```python
import win32com.client

#create an instance of Excel & make it visible
E = win32com.client.Dispatch("Excel.Application")
E.Visible = True

display(E)
# <COMObject Excel.Application>
```

After we start Excel Application, we add a Workbook object called book using the Add() method.

 display each object, notice how they're win32com.gen_py. objects that belong to our Microsoft Application.

```python
book = E.Workbooks.Add()

#create a new sheet
ws = book.Worksheets.Add()

# speficy a range of cells
rng1 = ws.Range("A1:A10")
rng1.Value = 1

display(book)
# <COMObject Add>
display(ws)
# <COMObject Add>
display(rng1)
# <COMObject Range>
display(rng1.Value)
# ((1.0,),
#  (1.0,),
#  (1.0,),
#  (1.0,),
#  (1.0,),
#  (1.0,),
#  (1.0,),
#  (1.0,),
#  (1.0,),
#  (1.0,))
```

A range of cells is simply made up of smaller individual cells that have their own unique properties and methods.  In code below we define a second range of cells but this time using the <span class="coding">Cells</span> object.  We a for loop to loop through each cell, display the address, or display the value of that cell. 

The <span class="coding">Cell</span> object is defined by the coordinate system (x-axis, y-axis).  So Cells(1,2) is B1. 
```python
# set a reference to a range of cells
Cell1 = ws.Cells(1,2)
Cell2 = ws.Cells(7,2)
Rng2 = ws.Range(Cell1,Cell2)
Rng2.Value = 1

# count the cells in our range
print(Rng2.Cells.Count)
# 7
# get the cell address using a for loop
for cellItem in Rng2:
    print(cellItem.Address)
# $B$1
# $B$2
# $B$3
# $B$4
# $B$5
# $B$6
# $B$7    
# get the cell value using a for loop but this time using a range object.    
for i in range(len(Rng2)):
    print(cellItem.Value)
# 1.0
# 1.0
# 1.0
# 1.0
# 1.0
# 1.0
# 1.0
```

# Outlook

Sometimes at work you want to send many people emails but you want to appear to be personal.  Sending them one by one manually is very tedious. 

If you like to use the mouse, you can use Mail Merge.  Otherwise if you are like me who tries not to use the mouse you can send email one by one to as many people as you like and each would appear personal. 

Say if you are sending each of your direct reports an email to let them know you are going to check on how they are doing, here is an example. It uses the <span class="coding">win32com.client</span> method from the <span class="coding">win32com</span> library, and specifically the <span class="coding">win32.Dispatch('outlook.application')</span> is for Outlook. 

Note:
Do not put any code comments within the HTML body <span class="coding">mail.HTMLBody</span> because otherwise they will appear in the email.  

<div class="code-head"><span>code</span>outlook.py</div>

```py
import win32com.client as win32
from datetime import datetime
import os
import pandas as pd
def email(EMAIL, FIRSTN):
    """
    input: EMAIL address, and FIRST NAME
    input: email body and subject
    """
    O = win32.Dispatch('outlook.application')
    mail = O.CreateItem(0)
    mail.Subject = 'My Subject ' + datetime.now()+strftime('%#d %b %Y %H:%M') # can remove the datetime if you don't want to have it in the subject
    mail.To = EMAIL
    mail.HTMLBody = r"""
    Dear """ + FIRSTN + r""", <br><br>
    I would like to schedule a quick call with you to learn about what you are doing. <br><br>
    I will send an invite. <br><br>
    Best regards, <br>
    Sarah
    """ 
    mail.Send()

df = pd.read_excel(r"myContactDirectory.xlsx")
df1 = df[df['manager name']=='Sarah Chen'].copy()
df1.reset_index(inplace=True)
df2= df1[['Name','ID']]
df2[['lastN','firstN']] = df2.Name.str.splilt(",", n=1, expand=True)
df2[['firstN1','firstN2']] = df2.Name.str.splilt() # incase someone has middle name

for i in range(df2.shape[0]):
    FIRSTN = df2.firstN[i]
    ID = df2.ID[i]
    EMAIL = ID+'@CompanyName.com'
    send_email(EMAIL, FIRSTN) # sending email to everyone

```

Yes, it is that simple. 

You can add images and attachments too.  

# PowerPoint
For Powerpoint, <span class="coding">pptx</span> is one other library.  I find it easy to use. 

## Create dashboard
In the code below, I create a Powerpoint presentation or dashboard of 9 timeseries with a header and footer textboxes filled with text hardcoded or imported.  We can specify font type, size, color and whether we want text wrapping. 

We have already created the 9 timeseries plots and saved them individually in our images folder. These 9 timeseries can be major economic indicators, key commodity prices, foreign exchange rates, swap rates, stock indices, etc.  


**Presentation.slide_layouts[6]**: we choose blank layout so that we can customize it. 

**slide.shapes.add_textbox(left, top, width, height)**: allows us to add arbitrary textboxes anywhere on the slide. 

Again, as we are going to use the Windows API, we have to follow Window's object defintions and their attribute/methods ladder. 

<div class="code-head"><span>code</span>pptx.py</div>

```python
from pptx import Presentation
from pptx.util import inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
cols = ['ts1', 'ts2', 'ts3', 'ts4', 'ts5', 'ts6'] # a list of time series names, e.g. CPI, GPP, etc. 
prs = Presentation()
blank_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_layout)
left = Inches(0.25)
top = Inches(0.25)
width = Inches(9.6)
height = Inches(1)
txBox = slide.shapes.add_textbox(left, top, width, height)
tf = txBox.text_frame
tf.word_wrap = True
p = tf.add_paragraph()
p.text = "Dashboard %s"%TODAY # TODAY is a string variable that I use for today's date
p.font.size = Pt(16)
run = p.add_run()
run.text = "Today's headlines are blahblahblah"
run.font.color.rgb = RGBColor(95, 95, 95)
run.font.size = Pt(11)
# row 1
img_path1 = "./images/%s_%s.png"%(cols[0], TODAY)
left = Inches(0.25)
top = Inches(1.25)
pic = slide.shapes.add_picture(img_path1, left, top)

img_path2 = "./images/%s_%s.png"%(cols[1], TODAY)
left = Inches(3.4)
top = Inches(1.25)
pic = slide.shapes.add_picture(img_path2, left, top)

img_path3 = "./images/%s_%s.png"%(cols[2], TODAY)
left = Inches(6.55)
top = Inches(1.25)
pic = slide.shapes.add_picture(img_path3, left, top)
# row 2
img_path4 = "./images/%s_%s.png"%(cols[3], TODAY)
left = Inches(0.25)
top = Inches(3.25)
pic = slide.shapes.add_picture(img_path4, left, top)

img_path5 = "./images/%s_%s.png"%(cols[4], TODAY)
left = Inches(3.4)
top = Inches(3.25)
pic = slide.shapes.add_picture(img_path5, left, top)

img_path6 = "./images/%s_%s.png"%(cols[5], TODAY)
left = Inches(6.55)
top = Inches(3.25)
pic = slide.shapes.add_picture(img_path6, left, top)
# row 3
img_path7 = "./images/%s_%s.png"%(cols[6], TODAY)
left = Inches(0.25)
top = Inches(5.25)
pic = slide.shapes.add_picture(img_path7, left, top)

img_path8 = "./images/%s_%s.png"%(cols[7], TODAY)
left = Inches(3.4)
top = Inches(5.25)
pic = slide.shapes.add_picture(img_path8, left, top)

img_path9 = "./images/%s_%s.png"%(cols[8], TODAY)
left = Inches(6.55)
top = Inches(5.25)
pic = slide.shapes.add_picture(img_path9, left, top)

# adding footer
top = Inches(6.95)
width = Inches(9.6)
height = Inches(0.05)
txBox = slide.shapes.add_textbox(left, top, width, height)
ft = txBox1.text_frame
ft.word_wrap  = True
p.text = "Source of data: FRED, IMF, etc"
p.font.size = Pt(8)
run.font.color.rgb = RGBColor(90, 90, 90) # lighter color for footer

# save pptx
prs.save("my_presentation%s.pptx"%TODAY)
```

## Copy from Excel to PowerPoint
Copying tables, charts and heatmaps from Excel to PowerPoint is something that office workers do all the time.  

**Copy from Excel tables to PowerPoint**
This example references code from [Sigma Coding's Github](https://github.com/areed1192/sigma_coding_youtube/blob/master/python/python-vba-powerpoint/Win32COM%20-%20PowerPoint%20To%20Excel%20-%20Chart%20Objects.py).  


<div class="code-head"><span>code</span>Excel range to pptx.py</div>

```python
import win32com.client
from win32com.client import constants as c
# Grab the Active Instance of Excel.
ExcelApp = win32com.client.GetActiveObject("Excel.Application")
ExcelApp.Visible = True # this is optional
wb1 = ExcelApp.Workbooks.Open(r"C:/users/SarahChen/RangeBook.xlsm")
# create a dictionary object
d = {}
for namedRng in wb1.Names:
    rngIdx = namedRng.Index
    rngName = namedRng.Name
    d[rngIdx] = rngName
print(d)

PPTApp = win32com.client.gencache.EnsureDispatch("PowerPoint.Application")
PPTApp.Visible = True
# Add a presentation to the PowerPoint Application, returns a Presentation Object.
PPTPresentation = PPTApp.Presentations.Add()
for key, value in d.items():
    PPTslide = PPTPresentation.Slides.Add(Index = key, Layout = 12) # 12 is blank layout
    ExcelApp.Range(value).Copy()
    PPTSlide.Shapes.PasteSpecial(DataType = 10, Link = True) # 10 is a ELEObject
```

**Copy from Excel charts to PowerPoint**

<div class="code-head"><span>code</span>Excel charts to pptx.py</div>

```python
# Grab the workbook with the charts.
wb = ExcelApp.Workbooks("MyChartObjects.xlsm")
# Create a new instance of PowerPoint and make sure it's visible.
PPTApp = win32com.client.gencache.EnsureDispatch("PowerPoint.Application")
PPTApp.Visible = True
# Add a presentation to the PowerPoint Application, returns a Presentation Object.
PPTPresentation = PPTApp.Presentations.Add()
# Loop through each Worksheet.
for xlWorksheet in wb.Worksheets:
    # Grab the ChartObjects Collection for each sheet.
    xlCharts = xlWorksheet.ChartObjects()
    # Loop through each Chart in the ChartObjects Collection.
    for index, xlChart in enumerate(xlCharts):
        # Each chart needs to be on it's own slide, so at this point create a new slide.
        PPTSlide = PPTPresentation.Slides.Add(Index = index + 1, Layout = 12)  # 12 is a blank layout
        # Display something to the user.
        print('Exporting Chart {} from Worksheet {}'.format(xlChart.Name, xlWorksheet.Name))
        # Copy the chart.
        xlChart.Copy()
        # Paste the Object to the Slide
        PPTSlide.Shapes.PasteSpecial(DataType = 1) 
# Save the presentation.
PPTPresentation.SaveAs(r"FILE_PATH")
```

# Run VBA code from Python

For non-VBA folks, you can run existing VBA code inherited from somewhere from Python.   The VBA code can be saved in the Excel file that you are to run. 
