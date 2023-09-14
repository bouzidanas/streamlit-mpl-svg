from mpl_svg import svg_plot

import matplotlib.pyplot as plt
from matplotlib import font_manager

font_dir = ['./fonts']
for font in font_manager.findSystemFonts(font_dir):
    font_manager.fontManager.addfont(font)

plt.rcParams.update({'font.family':"Source Code Pro"}) 

__all__ = [svg_plot]