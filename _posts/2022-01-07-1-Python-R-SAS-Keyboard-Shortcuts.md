---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Keyboard Shortcuts"
description: comparing Python, R and SAS everyday keyboard shortcuts
author: Sarah Chen
image: images/posts/photos/IMG-0685.jpg

---
![](/images/posts/photos/IMG-0685.jpg)
- [Keyboard shortcuts](#keyboard-shortcuts)
  - [VSCode](#vscode)
  - [RStudio](#rstudio)
- [Add custom snippets](#add-custom-snippets)

# Keyboard shortcuts
Keyboard shortcuts are essential because: when we are used to writing in a language, switching to another one can make use feel slow and dumb. Using keyboard shortcuts will allow us to pick up speed and feel at home. 

## VSCode
Although Spyder and Ipython (notebook and shell) both are great, VSCode is especially useful when we are writing packages or modules.  I use VSCode for all three languages.  There are suggested add-ons for each of the languages. 
See [keyboard shortcuts pdf](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf) for the comprehensive list.  
<!-- if image not shown, check if it is pushed yet, and case must match what's in github https://github.com/PythonRSAS/pythonrsas.github.io/tree/master/images/posts -->
![VSCode Keyboard Shortcuts](/images/posts/vscode_shortcuts.PNG)
You can also define your own keyboard shortcut. 

## RStudio 
- <span class="coding">Ctrl+Enter </span>  To run a line of code from the source editor.
- <span class="coding">Ctrl+Shift+M </span> is the pipe operator <span class="coding"> %>%</span> is or <span class="coding">Cmd+Shift+M</span> (Mac).
- <span class="coding">Alt + - </span> is the assignment operator <span class="coding"><-</span>, or Option + - (Mac).
- <span class="coding">Ctrl+L</span> to clear all the code from your console.
- <span class="coding">Ctrl+2 </span> and `Ctrl+1` to move the curser back and forth the source editor.
- <span class="coding">Ctrl + ↑</span>  to scroll through your command history by clicking  or Cmd + ↑ (Mac). 
- Search a matching subset of the history: type the first few characters and then press `Ctrl/Cmd + ↑`
- Rename all instances of a variable name: highlight one instance of the variable name and then using Code > *Rename in Scope*. This is better than using Edit > Replace and Find because it only looks for whole word matches.
  
# Add custom snippets
Using custom snippets helps save time.  Using 3 languages has a lot of syntax and libraries to remember.  
See [how to add a snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets) for details.

1. Use [snippet generator](https://snippet-generator.app/) to easily create the snippet json code.
2. <span class="coding">shift + command + p</span> and type <span class="coding">snippets</span>, and then  <span class="coding">Preferences: Configure User Snippets</span>. 
3. Hit <span class="coding">New snippets</span>, then choose language, and follow the directions.  Note, while the snippet is in json, you don't choose json.  Choose Python if the snippet is for Python code, choose markdown if it is for markdown. 