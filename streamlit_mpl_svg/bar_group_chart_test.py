import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from mpl_svg import svg_plot

value = st.slider("Slider", 0.0, 0.5, 0.01)

species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

html, svg, css = svg_plot(fig, id="first-bar", styling={"background": "#ffffff00", "title-color": "skyblue", "plot-area-border": "#ffffff", "plot-area-border-top": "#ffffff00", "plot-area-border-right": "#ffffff00", "axes-marks-color": "#ffffff", "y-axis-label-color": "skyblue"})

st.markdown(html, unsafe_allow_html=True)
st.code(css, language="css")