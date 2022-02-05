---
layout: post
tag : email, automation, python
category: "Python for SAS"
title: "Sending Work Email Using Python"
description: Sending individual email to many people Using Python at work
author: Sarah Chen
image: images/posts/photos/IMG-0688.jpg

---
![](images/posts/photos/IMG-0687.jpg)

Sometimes at work you want to send many people emails but you want to appear to be personal.  Sending them one by one manually is very tedious. 

If you like to use the mouse, you can use Mail Merge.  Otherwise if you are like me who tries not to use the mouse you can send email one by one to as many people as you like and each would appear personal. 

Say if you are sending each of your direct reports an email to let them know you are going to check on how they are doing, here is an example. It uses the <span class="coding">win32com.client</span> method from the <span class="coding">win32com</span> library, and specifically the <span class="coding">win32.Dispatch('outlook.application')</span> is for Outlook. 

> Note:
1. Do not put any code comments within the HTML body <span class="coding">r""" """</span> because they will appear in the email.  
2. The HTML <span class="coding"><br></span> means new line. 

<div class="code-head"><span>code</span>outlook.py</div>

```py
import win32com.client as win32
from datetime import datetime
import os
import pandas as pd
def email(EMAIL, FIRSTN):
    """
    input: EMAIL address, and FIRST NAME
    """
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
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

df = pd.read_excel(r"myContactDirect8ory.xlsx")
df1 = df[df['manager name']=='Sarah Chen'].copy()
df1.reset_index(inplace=True)
df2= df1[['Name','ID']]
df2[['lastN','firstN']] = df2.Name.str.splilt(",", n=1, expand=True)
df2[['firstN1','firstN2']] = df2.Name.str.splilt() # incase someone has middle name

for i in range(df2.shape[0]):
    FIRSTN = df2.firstN[i]
    ID = df2.ID[i]
    EMAIL = ID+'@CompanyName.com'
    send_email(EMAIL, FIRSTN)

```

Yes, it is that simple. 

You can add images and attachments too.  I won't get into it for now. 