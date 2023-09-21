streamlit-mpl-svg  [![Version](https://img.shields.io/pypi/v/streamlit-mpl-svg)](https://pypi.org/project/streamlit-mpl-svg/#history) 
[![PyPi - Downloads](https://img.shields.io/pypi/dm/streamlit-mpl-svg)](https://pypi.org/project/streamlit-mpl-svg/#files) [![Component Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mpl-svg-demo.streamlit.app/)
============

Reformat Matplotlib SVGs for easier access and customzation with CSS

## Installation
Install [streamlit-mpl-svg](https://pypi.org/project/streamlit-mpl-svg/) with pip:
```bash
pip install streamlit-mpl-svg
```

## Overview
This package provides tools for reformatting matplotlib figures with the end result being an SVG with accompaning CSS. The core motivations/intentions behind this package include:
- make it easier to target plot elements with CSS, 
- automatically size SVG to fit parent Streamlit containers,
- make changes to Matplotlib SVG without altering structure (moving or removing elements from the SVG DOM tree or adding elements to it) or changing the core nature of the SVG's elements (like element types),
- focus on the main important visual elements and characteristics rather than pass through Matplotlibs large, complex list of customization parameters (note: users should still be able to customize matplotlib plots the usual way if they so choose),
- provide a static CSS template for reusability,
- enable transition behavior by using single step CSS transitions and working with Streamlit's data flow model to stitch the steps together

## Usage

The `svg_plot` function takes, at a minimum, a Matplotlib figure and outputs a dictionary containing markup text of the formatted SVG, the CSS containing customizations in appearance (which can also be used as a template), and the two combined for quick and easy injection via `st.markdown` (with `unsafe_allow_html=True`) or via `st.components.v1.html`. 

`svg_plot` also takes a dictionary of visual parameters that makes changes to the outputted CSS:

### Example: styling dict
```python
{
 "background": "#ffffff"
 "plot-area-background": "#ffffff00"
 "plot-area-border": "#000000"
 "plot-area-border-top": "#000000"
 "plot-area-border-bottom": "#000000"
 "plot-area-border-left": "#000000"
 "plot-area-border-right": "#000000"
 "plot-area-border-width": "0.8"
 "plot-area-text-color": "#000000"
 "title-color": "#000000"
 "axes-marks-color": "#000000"
 "axes-marks-width": "1px"
 "x-axis-label-color": "#000000"
 "x-axis-marks-color": "#000000"
 "x-axis-text-color": "#000000"
 "x-axis-marks-width": "1px"
 "y-axis-label-color": "#000000"
 "y-axis-marks-color": "#000000"
 "y-axis-text-color": "#000000"
 "y-axis-marks-width": "1px"
 "plot-line-color": "#389734"
 "plot-line-width": "1.5"
 "legend-background": "#ffffff00"
 "legend-border-color": "#ffffff00"
 "legend-border-width": "1px"
 "legend-text-color": "#000000"
}
```

### Example: Bar Plot 
```python
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
```

## Transitions:

`svg_plot` provides one more additional element in its output - the transition dictionary. This dictionary contains necessary info to generate CSS transitions on certain types of SVG elements. 

### Example

```python
# Store previously generated SVG in session state
if "svgb" not in st.session_state:
    st.session_state["svgb"] = ""
        
# SVG plot container
bar_chart_container = st.container()
# Slider to control some of the bar heights
value = st.slider("Multiplier", 0.1, 1.0, 1.0)

# --------------- Matplotlib code ---------------
fig, ax = plt.subplots()
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [30, 100*value, 30*value, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.set_ylim(0, 100)

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color', x=0.5, y=1.05)
ax.legend(title='Fruit color')
# -----------------------------------------------

transitions = get_transitions(fig)
formatted_plot = svg_plot(fig, id="bar", styling=styling, transition_to=transitions)

# We want to use the svg in its previous state to transition inner elements to their new states
if st.session_state["svg"] == "":
    last_svg = formatted_plot["svg"]
else:
    last_svg = st.session_state["svg"]

# Update the svg in the session state
st.session_state["svg"] = formatted_plot["svg"]

# Construct the html markup from the svg and css
current_css = formatted_plot["css"]                           # contains current css transitions and styling
new_html = "<style>" + current_css + "</style>" + last_svg    # combine the current css and LAST svg

# Display the SVG (html markup) in the positioned container
with bar_chart_container:
    st.markdown(new_html, unsafe_allow_html=True)
```

## Limitations

- Transitions and custom CSS can break when the SVG DOM tree structure changes. Best practice is to Fix axes (fix range) and not to move `x` or `y` position of elements such that they lie outside of the SVG.
- Currently, transitions are only applied to bars (in bar graphs), lines, and poly collections.
- Currently, transitions only apply to changes in the `d` property (not changes in translational properties like `x`, and `y`). 

## Demo [![Component Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mpl-svg-demo.streamlit.app/)
![streamlit-mpl-svg-demo](https://github.com/bouzidanas/streamlit-mpl-svg/assets/25779130/dc9a87a7-2f19-4d15-9e56-a30a3156ef73)

## License
This project is licensed under the [MIT License](LICENSE.txt)