---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "mastering directories"
description: Understanding use of path in a Python program
author: Sarah Chen
image: images/posts/photos/IMG-0685.JPG

---
Say we are doing some data analysis.  And we have the following folder structure:
```
 --code/
 --lib/
 --data/
```

|  Type of files     | Input folder       | Output folder |
|:-------------------|:-------------------|:-------------------|
| code | code| images, analysis|
| input data | data| images, analysis|


We want to read data from the data folder, run code from the code folder, and output our analysis results with plots in .png and analysis in .txt files.

# "\"  vs "/"
<!-- When running SAS programs in SAS EG, we never ran into any problem directly pasting the address from Windows directory.  But for running Python and R programs, we need to deal with this small inconvinience.  -->

On Windows, paths are written using backslashes (\, the key with "|") as the separator between folder names. 

OS X and Linux, however, use the forward slash (/, the key with "?") as their path separator.

I really hate having to remember these confusing details.  They are not my loved ones' birthdays. 

#### Solution 1. Double \\
Two wrongs make it right.  Just double it up. Use it with full path name. 

#### Solution 2. Add 'r'
Ask Python to do the job and read it. Use it with full path name. 

#### Solution 3. os.path.join()
Use it with (full path name - relative directory). 

Paying the price of some extra typing, the <span class="coding">os.path.join()</span> function helps solving this problem. os.path.join() glues the steps of path together using the correct path separators.  
<div class="code-head">slashes.py</div>

```python
>>> df = pd.read_csv("C:\Users\sache\OneDrive\Documents\python_SAS\df4.csv")
  File "<ipython-input-8-24f5fb082f1d>", line 2
    df = pd.read_csv("C:\Users\sache\OneDrive\Documents\python_SAS\df4.csv")
                    ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

# Solution 1. Double \\
>>> df = pd.read_csv(r"C:\Users\sache\OneDrive\Documents\python_SAS\data\df4.csv")
# Solution 2. Add 'r'
>>> df = pd.read_csv("C:\\Users\\sache\\OneDrive\\Documents\\python_SAS\\data\\df4.csv")
# Solution 3. os.path.join
>>> df = pd.read_csv(os.path.join('.','OneDrive\Documents\python_SAS\data\df4.csv'))
```

# Get directory and change directory
When we need to know where we are, use os.getcwd().   To change that, use os.chdir() with full path as the parameter or use "./" with relative path. 
<div class="code-head"><span>code</span>learn_path.py</div>
```python
>>> os.getcwd()
'C:\\Users\\sache'
>>> os.listdir()
Out[17]:
['.anaconda',
 '.bash_history',
 '.bundle',
 '.cache',
 '.conda',
 '.condarc',
 '.gem',
>>> os.chdir('./OneDrive')
Out[19]: 'C:\\Users\\sache\\OneDrive'
```

# Create directory
When we run a lot of analysis, we can automate creating the directories. 

```
if not os.path.exists("images"):
    os.makedirs("images")
```

# Absolute path
Asolute path is the full path that we get from the address bar in Windows. <span class="coding">os.path.abspath</span>

<div class="code-head"><span>code</span>learn_path.py</div>

```python
In [1]: import os
        os.path.abspath('.')
Out[1]: 'C:\\Users\\sarahchen'

In [2]: os.path.abspath('.\\onedrive')
Out[2]: 'C:\\Users\\sarahchen\\onedrive'

In [3]: os.path.isabs(os.path.abspath('.'))
Out[3]: True

In [4]: os.path.relpath('C:\\Windows', 'C:\\')
Out[4]: 'Windows'

In [5]: os.path.relpath('C:\\Windows', 'C:\\windows')
Out[5]: '.'

In [6]: os.path.relpath('C:\Windows', 'C:\windows')
Out[6]: '.'

In [7]: os.path.relpath('C:/Windows', 'C:/windows')
Out[7]: '.'
```

# Relative path

We can partition a full path name into parent and child: 
- os.path.==dirname==(path), the parent directory:  *before* the last slash in the path argument. 

- os.path.==basename==(path), the child: *after* the last slash in the path argument. 

When a script is executed through the commandline, <span class="coding">\__file__'</span> refers to the script file that is being run. os.path.abspath(__file__) gives the complete path, which means the folder path + the file name.  
In this case, the parent is the folder path, while the child is the file name. 

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

# Path of the program/module






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

# SAS
If you want a path that is relative to the path of the current program, you have to build it yourself. 
To get the path of the current program, use <span class="coding">SYSGET("SAS_EXECFILEPATH")</span> in a data step or <span class="coding">%qsysfunc(sysget(SAS_EXECFILEPATH))</span> in macro code.

Relative file paths in SAS are relative to the '**current directory**'. 
In SAS we can easily use relative path from the command line. Elsewhere we need to tell SAS what directory we want as the base path.

<div class="code-head"><span>code</span>learn_path.sas</div>

```sas
%let rundir = /root/test/test1/test2;

%include "&rundir/../../path.sas"; 
```
In SAS, there are special variables, such as <span class="coding">\__n__</span>, <span class="coding">\_type_</span>, Python has special variables as well.    When the Python interpreter reads a source file, it first defines some special variables such as <span class="coding">\__builtin__</span> and <span class="coding">\__doc__</span>. <span class="coding">\__name__ == '\__main__'</span> is another one of them.

The purpose of <span class="coding">\__name__ == '\__main__'</span> is to allow us to check if the scipt is being run directly.  The actions following <span class="coding">\__name__ == '\__main__'</span> is to happen only if the script is being run directly.  


# References
[Chapter 8 – Reading and Writing Files](http://automatetheboringstuff.com/chapter8/)