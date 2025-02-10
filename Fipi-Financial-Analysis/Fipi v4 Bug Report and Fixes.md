---
title: Fipi v4 Bug Report and Fixes
---
2025-02-09 17:55
Tags: [[Python]] [[Fipi]]

# Bugs to Fix:


# Features to Add:

Improved Color Pallettes for the graphs

Possible Re-Design of the NavigationToolBar Widget
# Fixes:

## Color Pallettes for the Graphs:

This is quite simple since the color pallette information for the graphs are just in a hashmap of pallette names as keys with the values set as a list of hex codes

```
graph_pallettes = {

    'flare': ['#fcc98d', '#fcbd74', '#e98d6b', '#e3685c', '#d63c56', '#c93673', '#9e3460', '#8f3371', '#6c2b6d', '#511852'],

    'forest': ['#46327e', '#365c8d', '#277f8e', '#1fa187', '#4ac16d', '#a0da39']

                   }
```
As you can see they are quite limited and unfinished
I want at least 2 different pallettes with at least 15 colors per pallette

Thinking for flare try to make it a faint yellow to orange then red then maroon then dark purple
After messing around in a quick hex mapper script:
```
import matplotlib.pyplot as plt

import matplotlib.colors as mcolors

import numpy as np

  

def hex_to_rgb(hex_color):

    hex_color = hex_color.lstrip('#')

    return tuple(int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4))

  

def display_colormap(hex_colors, name='custom_colormap'):

    rgb_colors = [hex_to_rgb(hex_color) for hex_color in hex_colors]

    cmap = mcolors.LinearSegmentedColormap.from_list(name, rgb_colors)

  

    x = np.arange(len(hex_colors))

    y = np.ones(len(hex_colors))

    plt.figure(figsize=(8, 2))

    plt.imshow([x], cmap=cmap, aspect='auto')

    plt.yticks([])

    plt.xticks(np.arange(len(hex_colors)), hex_colors, rotation=45, ha='right')

    plt.xlabel('Hex Colors')

    plt.title('Color Map from Hex Colors')

    plt.tight_layout()

    plt.show()

  

# Example usage:

#hex_colors = ['#fcc98d', '#fcbd74', '#e98d6b', '#e3685c', '#d63c56', '#c93673', '#9e3460', '#8f3371', '#6c2b6d', '#511852']

flarev1 = ['#000004', '#160b39', '#420a68', '#6a176e', '#932667', '#bc3754', '#dd513a', '#f37819', '#fca50a', '#f6d746', '#fcffa4']

forest = ['#302652', '#372b61', '#46327e', '#365c8d','#277f8e', '#008f8f', '#1fa187', '#4ac16d', '#a0da39', '#bbf556', '#e3fa70']

#forestv1 = ['#46327e', '#365c8d', '#277f8e', '#1fa187', '#4ac16d', '#a0da39']

#display_colormap(hex_colors)

display_colormap(flarev1, name='flarev1')

display_colormap(forest, name='forest')

#display_colormap(forestv1, name='forestv1')
```
I came around on two themes: flarev1 and forest

now implementing them possibly with a switch widget that changes the rest of the colors in the program to a green

to change every color in the program to a new pallette on switch I wrote two functions
one that would configure every element to the colors of the flare pallette and one that would do the same for the forest pallette

with 38 different widgets to reconfigure thats quite alot but it works without delay

a little quirk ive found is if you switch the pallette of the graph you have to click the graph button again because if you just go back to the graph page the color will still be what it was before and if you click the update button there, it will change all the other colors n=back to before you changed it so i added a warning on the import page later down the line ill fix that problem

Final Look:

Flare Theme:

![[orangetheme-fipi-v4.PNG]]

![[orangethemegraph-fipi-v4.PNG]]

forest theme:

![[greentheme-fipi-v4.PNG]]

![[greenthemegraph-fipi-v4.PNG]]

## Ugly Navigation Toolbar Problem

The only reason I used this feature in the first place was to avoid writing my own save figure function and button, that utility bar is ver ymuch an eyesore

Now to remedy that with my own button


# Report:

# Notes:

Yes for the astute among you the flare pallette is literally the flare theme from seaborn with a few extra tweaks to it and the starting forest pallette is the viridis theme verbatim
