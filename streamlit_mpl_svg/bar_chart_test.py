import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from streamlit_mpl_svg import svg_plot

value = st.slider("Slider", 0.1, 1.0, 0.1)

figure, axes = plt.subplots()
x = np.arange(0,4,1)
y = 25*x + 25

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100*value, 30, 55]                    # <-- Slider changes the second value

axes.bar(fruits, counts)
axes.plot(x, y, color="red", linewidth=5)

axes.set_ylabel('fruit supply')
axes.set_title('Fruit supply by kind and color')

styling = {
    "background": "#ffffff00",
    "title-color": "skyblue",
    "plot-area-border": "#ffffff",
    "plot-area-border-top": "#ffffff00",
    "plot-area-border-right": "#ffffff00",
    "axes-marks-color": "#ffffff",
    "y-axis-label-color": "skyblue"
}

formatted_plot = svg_plot(figure, styling=styling)

st.markdown(formatted_plot["html"], unsafe_allow_html=True)