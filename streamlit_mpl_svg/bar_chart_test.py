import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from mpl_svg import svg_plot

value = st.slider("Slider", 0.0, 0.5, 0.01)

figure, axes = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]

axes.bar(fruits, counts)

axes.set_ylabel('fruit supply')
axes.set_title('Fruit supply by kind and color')

html, svg, css = svg_plot(figure, styling={"background": "#ffffff00", "title-color": "skyblue", "plot-area-border": "#ffffff", "plot-area-border-top": "#ffffff00", "plot-area-border-right": "#ffffff00", "axes-marks-color": "#ffffff", "y-axis-label-color": "skyblue"})

st.markdown(html, unsafe_allow_html=True)
st.code(css, language="css")