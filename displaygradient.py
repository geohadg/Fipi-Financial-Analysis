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
flarev1 = ['#160b39', '#420a68', '#6a176e', '#932667', '#bc3754', '#dd513a', '#f37819', '#fca50a', '#f6d746', '#fcffa4']
forest = ['#302652', '#372b61', '#46327e', '#365c8d','#277f8e', '#008f8f', '#1fa187', '#4ac16d', '#a0da39', '#bbf556', '#e3fa70']
forestv2 =   ["#6fff00", "#49ff00", "#00fb11", "#00ff38", "#00ff6b"]
#forestv1 = ['#46327e', '#365c8d', '#277f8e', '#1fa187', '#4ac16d', '#a0da39']
#display_colormap(hex_colors)
display_colormap(flarev1, name='flarev1')
display_colormap(forestv2, name='forest')
#display_colormap(forestv1, name='forestv1')