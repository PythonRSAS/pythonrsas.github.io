---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "SAS PROC SQL and python df.groupby and pivot_table, and simple joins"
description:  On python pandas groupby, pivot_table and other methods and compare them to SAS PROC SQL, which is like most SQL
author: Sarah Chen
image: images/posts/photos/IMG-0672.JPG

---
<figure> 
   <img src="{{"/images/photos/posts/IMG-0672.jpg"| relative_url}}"> 
   <figcaption>Photo by Ji Biduan</figcaption>
</figure> 


# view vs copy
view gives you the original data
copy gives you a copy.  Changes made to the copy won't affect the original data. 

Most pandas operations return copies. To make the changes stick, we would need to assign it to a name or overwrite it using the same name. 

# describe

Below is a simple select statement,selecting all the columns, using a where statement to filter. 
<div class="code-head"><span>code</span>describe.sas</div>

```sas
PROC SQL;
DESCRIBE TABLE df;
```

In Python, 
```python
df.info()
```

# Rows and columns


<div class="code-head"><span>code</span>groupby.py</div>

```python
tips= sns.load_dataset('tips')
tips.groupby(['smoker', 'day']).agg({'tip': [np.size, np.mean]})
Out: 
               tip
              size  mean
smoker day
Yes    Thur 17.000 3.030