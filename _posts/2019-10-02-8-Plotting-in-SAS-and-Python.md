---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Plotting in SAS and Python"
description: Various essential plots using Python and SAS.
author: Sarah Chen
image: http://drive.google.com/uc?export=view&id=1hXH-eJF20B6xAJvc1W5icAzePG1MwUuO

---

In this post (partially taken from my upcoming book), we go over a few very commonly used plots and compare the code in SAS, Python, and ways to save images.  For non-SAS users, we intentionally upcase the SAS keywords, even though SAS is not case-sensititve.  

**- [Bar-line plot](#Bar-line-plot)**

[Period](#Period)

**- [Saving Images](#Saving-Images)**

**- [Title Footnote and Annotations](#Enhance-Images)**

<figure>
  <img src="{{ "/images/posts/PythonVisLandscape2018.jpg" | relative_url }}">
  <!-- <figcaption> source</figcaption> -->
</figure>
Let's get started.

<h4 id="Bar-line-plot">Bar-line plot</h4>

One of the most commonly used plots in business is the bar-line plot, where bars are for frequency and lines are for aggregations such as sum, mean or median. 

<div class="code-head"><span>code</span>Bar-line plots.sas</div>

```sas
ODS GRAPHICS ON / WIDTH=12IN HEIGHT=5IN;
PROC SGPLOT DATA=df;
    VBAR date/ DATASKIN=PRESSED FILLATTRS=(COLOR=LIGGR);
    VLINE date/RESPONSE=X1 STAT=MEAN LEGENDLABEL ='  ' Y2AXIS LINEATTRS=(THICKNESS=1.5 PATTERN=SOLID     COLOR=RED) Y2AXIS;
    VLINE date/RESPONSE=X2 STAT=MEDIAN LEGENDLABEL ='  ' Y2AXIS LINEATTRS=(THICKNESS=1.5 PATTERN=SOLID     COLOR=MEDIUMBLUE) Y2AXIS;
    YAXIS VALUES=(0, 100) OFFSETMIN=0 LABEL = "volumn";
    Y2AXIS GRID VALUES=(0, 10, 100,1000) OFFSETMIN=0 LABEL = "X1";
    XAXIS VALUES=(   );
    INSET "your text for annotation"/POSITION =TOP;
RUN;
```

Note:
 - The VBAR statement produces vertical bar charts and HBAR produces horizontal bar charts.   By default, frequency counts for each category are plotted.  This is very convenient: no need to run PROC SQL group by or PROC MEANS summarize by CLASS prior to plotting. 
  - When the <span class='coding'>RESPONSE</span> option is speciﬁed, summary statistics (sums, means, etc.) can be plotted separately for each category of the speciﬁed response variable.

<div class="code-head"><span>code</span>Bar-line plots.python</div>

```python

```

The SERIES statement produces time series plots.

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