---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "mastering directories"
description: Understanding use of path in a Python program
author: Sarah Chen
image: images/posts/photos/IMG-0685.JPG

---
Say we are doing some data analysis.  And we have the following folder structure: code, data. 

|  Type of files     | Input folder       | Output folder |
|:-------------------|:-------------------|:-------------------|
| code | code| images, analysis|
| input data | data| images, analysis|

We want to read data from the data folder, run code from the code folder, and output our analysis results with plots in .png and analysis in .txt files.

# "\\"  or "/"
<!-- When running SAS programs in SAS EG, we never ran into any problem directly pasting the address from Windows directory.  But for running Python and R programs, we need to deal with this small inconvinience.  -->

On Windows, paths are written using backslashes (\, the key with "|") as the separator between folder names. 

OS X and Linux, however, use the forward slash (/, the key with "?") as their path separator.

I really hate having to remember these confusing details.  And I don't like
`path=dir + '/' + subdir + '/'+filename`, although it is equivalent to `path=os.path.join(dir,subdir,filename)`

#### Solution 1. Double \\
Two wrongs make it right.  Just double it up. Use it with full path name. 

#### Solution 2. Add 'r'
Ask Python to do the job and read it. Use it with full path name. 

#### Solution 3. os.path.join()
Use it with (full path name - relative directory). 

With some extra typing, the <span class="coding">os.path.join()</span> function helps solving this problem. os.path.join() glues the  path pieces together using the correct path separators.  
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

# Get directory, content and change directory
When we need to know where we are, use os.getcwd().   To change that, use os.chdir() with full path as the parameter or use "./" with relative path. 
os.path.getsize

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
In [30]: os.path.getsize(path)
Out[30]: 65536
```

# Create directory
When we run a lot of analysis, we can automate creating the directories. 

```
if not os.path.exists("images"):
    os.makedirs("images")
```

# Absolute path
Asolute path is the full path that we get from the address bar in Windows. <span class="coding">os.path.abspath</span>
<span class="coding">os.path.relpath</span> gives the difference between two input paths. 
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

<div class="code-head"><span>code</span>run_result_of_learn_path.py</div>

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

# Partitioning a path

### folder name and file name
We can partition a full path name into parent and child: 
<span class="coding">os.path.==dirname==(path)</span>, the parent directory:  *before* the last slash in the path argument. 

<span class="coding">os.path.==basename==(path)</sapn>, the child: *after* the last slash in the path argument. 

When a script is executed through the commandline, <span class="coding">\__file__'</span> refers to the script file that is being run. <span class="coding">os.path.abspath(\__file__)</span> gives the complete path, which means the folder path + the file name.  
In this case, the parent is the folder path, while the child is the file name. 

<div class="code-head"><span>code</span>learn_path1.py</div>

```python
import os
ABS_PATH = os.path.abspath(__file__)
print("\n ABS_PATH ", ABS_PATH)
PARENT_PATH = os.path.dirname(ABS_PATH)
print("\n PARENT_PATH ",PARENT_PATH)
CHILD_PATH = os.path.basename(ABS_PATH)
print("\n CHILD_PATH ",CHILD_PATH)

# The result of running the above code is as followed:

#(base) C:\Users\sache\OneDrive\Documents\python_SAS\Code_only>python learn_path2.py

# ABS_PATH  C:\Users\sache\OneDrive\Documents\python_SAS\Code_only\learn_path2.py

# PARENT_PATH  C:\Users\sache\OneDrive\Documents\python_SAS\Code_only

# CHILD_PATH  learn_path2.py
```

# split folder path
```python

{In [28]: path
Out[28]: 'C:\\Users\\sache\\OneDrive'

In [29]: os.path.split(path)
Out[29]: ('C:\\Users\\sache', 'OneDrive')}
```

# Grandparent and great grandparents

Using the same logic of getting the parent, we can access the grandparent directory using <span class="coding">os.path.dirname</span>. 

<div class="code-head"><span>code</span>parent.py</div>

```python
In [19]: os.getcwd()
Out[19]: 'C:\\Users\\sache\\OneDrive'
In [21]: os.path.dirname(path)
Out[21]: 'C:\\Users\\sache'
In [23]: os.path.dirname(os.path.dirname(path))
Out[23]: 'C:\\Users'
```

However, you cannot get grandchildren.
```python

{In [24]: os.path.basename(path)
Out[24]: 'OneDrive'

In [25]: os.path.basename(os.path.basename(path))
Out[25]: 'OneDrive'}
```

# Relative path and absolute path
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

In aside from the command line, elsewhere we need to tell SAS what directory we want as the base path.

<div class="code-head"><span>code</span>learn_path.sas</div>

```sas
%let rundir = C:/Users/sache/onedrive/;

%include "&rundir/../codeonly/path.sas"; 
```
Relative file paths in SAS are relative to the '**current directory**'. 
If you want a path that is relative to the path of the current program, you have to build it yourself. 
To get the path of the current program, use <span class="coding">SYSGET("SAS_EXECFILEPATH")</span> in a data step or <span class="coding">%qsysfunc(sysget(SAS_EXECFILEPATH))</span> in macro code.



