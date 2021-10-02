---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "configparser"
description: discuss configuration files 
author: Sarah Chen
image: images/posts/photos/IMG-0669.JPG

---
<figure> 
   <img src="{{"/images/posts/photos/IMG-0669.jpg"| relative_url}}"> 
</figure> 
When we work on a project in SAS, we often like to have a separate program for defining libnames, path, constant parameters, some macro variables, and filenames.  In Python, we like to do the same, except that we call it "configuration" or "config".  Of course, these concepts are not unique to Python or SAS. 

In Python, configuration is often done via .ini, .json, or a .py file.  Here I discuss the .ini approach using configparser library. 

We can read, update, add entry, create new sections using interpolation and extended interpolation. 

The beginning .ini file is as followed:

```python
[files]
data1 = data1.csv
data2 = data2.csv
data3 = data3.csv
new_data = 2021data.csv

[constants]
min_expense = 10

[path]
output = c:\analysis
```

We first import the configparser, tell it to read the .ini file.   
<div class="code-head"><span>code</span>read.python</div>

```python
In [1]: import configparser'
   ...: # In Python 3, configParser has been renamed to configparser '
   ...: config = configparser.ConfigParser()'
   ...: # config'
   ...: # <configParser.configParser instance at 0x00BA9B20>'
   ...: config.read(r"C:\Users\sache\OneDrive\Documents\python_SAS\Code_only\learn_ini.ini")

In [2]: config
Out[2]: <configparser.ConfigParser at 0x25391622a88>

In [3]: print(list(config['files'].keys()))'
   ...:
['data1', 'data2', 'data3', 'new_data']

In [4]: print(list(config['files'].values()))
['data1.csv', 'data2.csv', 'data3.csv', '2021data.csv']

In [5]: for sect in config.sections():'
   ...:     print("\nSection: ",sect)'
   ...:     for i,j in config.items(sect):'
   ...:         print("Key: ",i," Value: ",j)
   ...:
# Section:  files
# Key:  data1  Value:  data1.csv
# Key:  data2  Value:  data2.csv
# Key:  data3  Value:  data3.csv
# Key:  new_data  Value:  2021data.csv

# Section:  constants
# Key:  min_expense  Value:  10

# Section:  path
# Key:  output  Value:  c:\analysis
```
Explanation: and get a listing of the sections. Sections are listed in square brackets [].

Note: section names are case sensitive, but the keys are not case-sensitive.

# Updating the values

The following will overwrite a section of the .ini file.  It only overwrites the section specified and does not do it to the rest of the sections. 
<div class="code-head"><span>code</span>updateConfig.python</div>

```python
In [6]: filename = r"C:\Users\sache\OneDrive\Documents\python_SAS\Code_only\learn_ini.ini"'
   ...: config = configparser.ConfigParser()'
   ...: config.read(filename)'
   ...: # uppdates the entire 'files' section'
   ...: config['files']={'new_data' :'2021data.csv'}'
   ...: with open(filename, 'w') as configfile:'
   ...:     config.write(configfile)
# [files]
# data1 = data1.csv
# data2 = data2.csv
# data3 = data3.csv
# new_data = 2021data.csv

# [constants]
# min_expense = 10

# [path]
# output = c:\analysis
```

# update or add entries
If the section already exist, then it will be updated.  If it does not already exist, then a new section will be added. 
<div class="code-head"><span>code</span>update.python</div>

```python

In [8]: # creating the dictionary for section and key-value pairs'
   ...: config['goals']={'
   ...:     'revenue':200,'
   ...:     'customer count':30,'
   ...:     'profit':15'
   ...: }'
   ...: # writing to configuration file'
   ...: with open(filename, 'w') as configfile:'
   ...:     config.write(configfile)
```

# basic interpolation of values
Interpolation is when the value for the keys in the config files are preprocessed before returning them. 
The syntax for basic interpolation is: %(key_name)
This usage is similar to using %s for strings and %d for numbers. 

The following code updates section "path" that contains two keys "output" and "images". The value for key "images" will be created by substituting "output" using interpolation.


<div class="code-head"><span>code</span>interpolation.python</div>

```python
config['path']={
    'output' : r'c:\analysis',
    'images': '%(output)s\images'}
with open(filename, 'w') as configfile:
    config.write(configfile)
print(config["path"]['images'])
 
```
# extended interpolation
Extended interpolation is to preprocess and substitute values for a key from a **different** section of the configuration file before returning them.

The syntax for extended interpolation :${section:key}

The following code uses extended interpolation from the key "output" of the section "path".

To read the extended interpolation, we need to set the interpolation of the config file to ExtendedInterpolation() for dynamic substitution. 

<div class="code-head"><span>code</span>extended interpolation.python</div>

```python
# write using extended interpolation
config['results']={'customer' : '${path:output}\\customer',
                     'revenue':'${path:output}s\\revenue',
                     'profit':'${path:output}s\\profit'
                    }
with open(filename, 'w') as configfile:
    config.write(configfile)

# to read the extended interpolation
config._interpolation = configparser.ExtendedInterpolation()
config.read('test_config.ini')
print(config["results"]['customer'])
```
The end result, after all these updates, is as followed:
```python
[files]
new_data = 2021data.csv

[constants]
min_expense = 10

[path]
output = c:\analysis
images = %(output)s\images

[goals]
revenue = 200
customer count = 30
profit = 15

[results]
customer = ${path:output}\customer
revenue = ${path:output}s\revenue
profit = ${path:output}s\profit
```

