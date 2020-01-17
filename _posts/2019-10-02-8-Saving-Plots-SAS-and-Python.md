---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Saving Plots in SAS and Python"
description: Setting up and saving plots in Python and SAS.
author: Sarah Chen
image: http://drive.google.com/uc?export=view&id=1hXH-eJF20B6xAJvc1W5icAzePG1MwUuO

---

In this post (partially taken from my upcoming book), we go over how to set up your plotting enviroment and ways to save images.  For non-SAS users, we intentionally upcase the SAS keywords, even though SAS is not case-sensititve.  

**- [Saving Images](#Saving-Images)**

**- [Title Footnote and Annotations](#Enhance-Images)**

Let's get started.

<h3 id="Saving-Images">Saving Images</h3>

Of course, you can snip and save.  But here is how to automate it, and save in different formats/styles. 

**Python R SAS**
Menu-driven solution:
– Right-click on on a graphics window and save is as 

Output-file solution:
ODS (Output Delivery System) is a way to save high-quality output to different ﬁles with options for style templates:
– RTF ﬁles – PS (Postscript) ﬁles – PDF ﬁles – HTML ﬁles
– Selecting Create HTML... to save output in HTML format under Tools -> Options -> Preferences. 

<div class="code-head"><span>code</span>ODS.sas</div>

```sas
>>> ODS PDF FILE="C:\Users\SarahChen\python_R_SAS\images\filename.pdf";
# plotting code ...
>>> ODS PDF CLOSE;
```
Note:
- While savingfilename.pdf,an attractive PDF window will open in SAS.  This saves you the work having to find it and open it. 
<div class="code-head"><span>code</span>ODS Listing.sas</div>

```sas
>>> ODS LISTING CLOSE;
>>> ODS PDF FILE="c:\SarahChen\filename.pdf";
# plotting code ...
>>> ODS PDF CLOSE;
>>> ODS LISTING;
```
Note:
- <span class='coding'>ODS LISTING CLOSE</span> is used to turn off the default output device, and the default output device is resumed once we are finished with the block of code. 



As SAS users are aware, SAS procedures outputs can be way too much. 

```sas
>>> ODS TRACE ON;
SAS PROC 
>>> ODS TRACE OFF;
```
Note:
- <span class='coding'>ODS TRACE ON</span> writes names of outputs (tables and images) to the log. 
- <span class='coding'>ODS SELECT </span> is used to to choose a few selected pieces of the output.

```sas
<!-- SAS PROC  -->
>>> (SAS PROC statements) ODS name=your_out_name path=your_out_path; RUN;
```
Note:
- <span class='coding'>ODS TRACE ON</span> writes names of outputs (tables and images) to the log. 
- <span class='coding'>ODS SELECT </span> is used to to choose a few selected pieces of the output.

Using matplotlib you can use the savefig() function.  While it is most common to save plots as .png, it is nice to know that there are actually many options for file type.  All you have to do is change the file extension in the savefig(). 

However, as the function is only for saving figure, you cannot save figure and tables together like you do in SAS ODS. 

<div class="code-head"><span>code</span>save images.py</div>

```python
import matplotlib.pyplot as plt #for plotting
import os
os.chdir(r'C:\Users\SarahChen\python_R_SAS')
# plt.rcParams["axes.titlesize"] = 12
# titlesize': 12.0,  
root_path = "."

def save_fig(fig_name, tight_layout=True):
    path = os.path.join( root_path, '%s'%Project, "images",fig_name + ".png")
    print("Saving figure", fig_name)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format='png', dpi=350)

Project = 'plotting'
```

<h3 id="Enhance-Images">Title Footnote and Annotations</h3>

**SAS**

We can change the color, background color, height, font, etc. of titles and footnotes with options in the <span class='coding'>TITLE</span> and <span class='coding'>FOOTNOTE</span> statements. 
* Can make text justiﬁed or italic, as well. 
* The <span class='coding'>STYLE</span> option in <span class='coding'>PROC PRINT</span> can change the background color, text color, font style, etc., of data table cells, column headers, and other <span class='coding'>PROC PRINT</span> output. 
* Similar customization can be done to <span class='coding'>PROC REPORT</span> or <span class='coding'>PROC TABULATE</span>  output. 
* By deﬁning style formats with <span class='coding'>PROC FORMAT</span> , you can even alter the appearance of the output depending on the data value being printed (trafﬁc-lighting).