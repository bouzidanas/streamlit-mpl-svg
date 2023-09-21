import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from __init__ import svg_plot, get_transitions

if "transitions" not in st.session_state:
    st.session_state["transitions"] = {}
if "svg" not in st.session_state:
    st.session_state["svg"] = ""

value = st.slider("Slider", 0.1, 1.0, 0.1)

figure, axes = plt.subplots()
x = np.arange(0,4,1)
y = 25*x + 25

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100*value, 30, 55]

axes.bar(fruits, counts)
axes.plot(x, y, color="red", linewidth=5)

axes.set_ylabel('fruit supply')
axes.set_title('Fruit supply by kind and color')

transitions = get_transitions(figure)
formatted_plot = svg_plot(figure, styling={"background": "#ffffff00", "title-color": "skyblue", "plot-area-border": "#ffffff", "plot-area-border-top": "#ffffff00", "plot-area-border-right": "#ffffff00", "axes-marks-color": "#ffffff", "y-axis-label-color": "skyblue"}, transition_to=transitions)

if st.session_state["svg"] == "":
    last_svg = formatted_plot["svg"]
else:
    last_svg = st.session_state["svg"]

current_css = formatted_plot["css"]  # contains current css transitions

new_html = "<style>" + current_css + "</style>" + last_svg

st.session_state["svg"] = formatted_plot["svg"]

st.markdown(new_html, unsafe_allow_html=True)
st.code(formatted_plot["css"], language="css")