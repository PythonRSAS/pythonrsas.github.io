---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Keyboard Shortcuts"
description: comparing Python, R and SAS everyday keyboard shortcuts
author: Sarah Chen
image: images/posts/IMG-0669.JPG

---
Work in Progress.  Check back later. 

- [Keyboard shortcuts](#keyboard-shortcuts)
      - [VSCode](#vscode)
        - [Add custom snippets](#add-custom-snippets)
      - [RStudio](#rstudio)


# Keyboard shortcuts
Keyboard shortcuts are essential because:
When we are used to writing in a language, switching to another one can make use feel slow and dumb. Using keyboard shortcuts will allow us to pick up speed and feel at home. 

#### VSCode
Although Spyder and Ipython (notebook and shell) both are great, VSCode is especially useful when we are writing packages or modules.  I use VSCode for all three languages.  There are suggested add-ons for each of the languages. 
See [keyboard shortcuts pdf](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf) for a comprehensive list.  

You can also define your own keyboard shortcut. 

##### Add custom snippets
Using custom snippets helps save time.  Using 3 languages has a lot of syntax and libraries to remember.  
[how to add a snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets).
> `shift + command + p` and type snippets => Select `Preferences`: Open User Snippets 
[snippet generator](https://snippet-generator.app/)

#### RStudio 
- <span class="coding">Ctrl+Enter </span>  (Windows)To run a line of code from the source editor.
- <span class="coding">Ctrl+Shift+M </span>(Windows) is the pipe operator <span class="coding"> %>%</span> is or <span class="coding">Cmd+Shift+M</span> (Mac).
- <span class="coding">Alt + - </span>(Windows) is the assignment operator <span class="coding"><-</span>, or Option + - (Mac).
- <span class="coding">Ctrl+L</span> to clear all the code from your console.
- <span class="coding">Ctrl+2 </span> and `Ctrl+1` to move the curser back and forth the source editor.
- <span class="coding">Ctrl + ↑</span> (Windows) to scroll through your command history by clicking  or Cmd + ↑ (Mac). 
- Search a matching subset of the history: type the first few characters and then press `Ctrl/Cmd + ↑`
- Rename all instances of a variable name: highlight one instance of the variable name and then using Code > *Rename in Scope*. This is better than using Edit > Replace and Find because it only looks for whole word matches.