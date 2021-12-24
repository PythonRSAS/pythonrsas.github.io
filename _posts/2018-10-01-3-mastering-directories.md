---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "mastering directories"
description: Understanding use of path in a Python program
author: Sarah Chen
image: images/posts/photos/IMG-0685.JPG

---
Say we are doing some data analysis. Our code outputs plots in .png and analysis in .txt files. And we have the following folder structure:
```
 --code/
 --lib/
 --data/
```python
```
# Create directory

>>> import os
>>> os.makedirs('C:\\pythonrsas\\')
```

# Absolute path
<span class="coding">os.path.abspath</span>

```python
In [1]: import os
        os.path.abspath('.')
Out[1]: 'C:\\Users\\sarahchen'
In [2]: os.path.abspath('.\\onedrive')
Out[2]: 'C:\\Users\\sarahchen\\onedrive'
```

# Relative path
Relative file paths in SAS are relative to the '**current directory**'. 
In SAS we can easily use relative path from the command line. Elsewhere we need to tell SAS what directory we want as the base path.

<div class="code-head"><span>code</span>learn_path.sas</div>

```sas
%let rundir = /root/test/test1/test2;

%include "&rundir/../../path.sas"; 
```
# Path of the program/module
If you want a path that is relative to the path of the current program, you have to build it yourself. 
To get the path of the current program, use <span class="coding">SYSGET("SAS_EXECFILEPATH")</span> in a data step or <span class="coding">%qsysfunc(sysget(SAS_EXECFILEPATH))</span> in macro code.

<div class="code-head"><span>code</span>learn_path.py</div>



In SAS, there are special variables, such as <span class="coding">\__n__</span>, <span class="coding">\_type_</span>, Python has special variables as well.    When the Python interpreter reads a source file, it first defines some special variables such as <span class="coding">\__builtin__</span> and <span class="coding">\__doc__</span>. <span class="coding">\__name__ == '\__main__'</span> is another one of them.

The purpose of <span class="coding">\__name__ == '\__main__'</span> is to allow us to check if the scipt is being run directly.  The actions following <span class="coding">\__name__ == '\__main__'</span> is to happen only if the script is being run directly.  


The <span class="coding">os.path.dirname()</span> function removes the last segment of a path.
<span class="coding">__file__</span> is the pathname of the file from which the module was loaded, if it was loaded from a file.

<div class="code-head"><span>code</span>learn_path.py</div>

```python
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print("PROJECT_ROOT is ",PROJECT_ROOT)
BASE_DIR = os.path.dirname(PROJECT_ROOT)
print("BASE_DIR is",BASE_DIR)
# PROJECT_ROOT is  C:\python_SAS\Code_only
# BASE_DIR is C:\python_SAS
```

Now, open the command prompt, or Anaconda Prompt, type "python learn_path.py", as shown below, we will get the output as expected. Both the first and the second function ran.  The second function ran because the name of the module according to the Python interpreter, is <span class="coding">\__name__ == '\__main__'</span>. 

On the other hand, if a module is not the main program but is imported by another one, then <span class="coding">\__name__</span> attribute will be the name of the scirpt, in this case it is "learn_main", not <span class="coding">\__main__</span>.  Since the <span class="coding">\__name__</span> is not \__main__, then whatever \__main__ does will be ignored. 

This neat trick helps us reuse code more flexibly.  