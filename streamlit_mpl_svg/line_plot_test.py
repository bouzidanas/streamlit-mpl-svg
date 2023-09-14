import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from mpl_svg import svg_plot

value = st.slider("Slider", 0.0, 0.5, 0.01)

figure, axes = plt.subplots()
x = np.arange(0,100,0.01)
y = 0.5*x*np.sin(value*np.pi*x)
yb = 0.4*x*np.sin(value*np.pi*x)
plt.plot(x, y)
plt.plot(x, yb)

html, svg, css = svg_plot(figure, styling={"background": "#ffffff00", "plot-area-border": "#ffffff", "plot-area-border-top": "#ffffff00", "plot-area-border-right": "#ffffff00", "axes-marks-color": "#ffffff", "plot-line-color": ["#747484", "#2288aa"]})

st.markdown(html, unsafe_allow_html=True)
st.code(css, language="css")