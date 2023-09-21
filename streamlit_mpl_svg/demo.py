import matplotlib as mpl
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from streamlit_mpl_svg import *

st.set_page_config(page_title="Streamlit Matplotlib SVG Demo", page_icon=":bar_chart:")

if "svgb" not in st.session_state:
    st.session_state["svgb"] = ""
if "svgl" not in st.session_state:
    st.session_state["svgl"] = ""
if "svgm" not in st.session_state:
    st.session_state["svgm"] = ""

with st.sidebar:
    st.write("# Customize Matplotlib SVGs")
    on = st.toggle('Activate customizations')

    if on:
        st.write("## Customizations")
        cola, colb, colc = st.columns([1,1,0.5])
        font = cola.toggle("Streamlit font")
        if font:
            if plt.rcParams["font.family"][0] != "Source Code Pro":
                load_streamlit_default_fonts()
        else:
            mpl.rcParams.update(mpl.rcParamsDefault)

        dark = colb.toggle('Dark mode')
        if dark:
            background_color = "#0e1117"
            axes_default_color = "#ffffff"
            highlight_color = "#87CEEB"
        else:
            background_color = "#ffffff"
            axes_default_color = "#000000"
            highlight_color = "#5FA0B3"
        col1, col2 = st.columns([5,1])
        background_opacity = col1.slider("Background opacity", 0.0, 1.0, 1.0)
        background_color = col2.color_picker("Color", background_color, key="background-color")

        col7, col8 = st.columns([5,1])
        plot_area_border_opacity = col7.slider("Plot area border opacity", 0.0, 1.0, 1.0)
        plot_area_border = col8.color_picker("Color", axes_default_color, key="plot-area-border")

        col3, col4 = st.columns([5,1])
        title_opacity = col3.slider("Title opacity", 0.0, 1.0, 1.0)
        title_color = col4.color_picker("Color", highlight_color, key="title-color")

        col11, col12 = st.columns([5,1])
        x_axis_label_opacity = col11.slider("X axis label opacity", 0.0, 1.0, 1.0)
        x_axis_label_color = col12.color_picker("Color", highlight_color, key="x-axis-label-color")

        col13, col14 = st.columns([5,1])
        y_axis_label_opacity = col13.slider("Y axis label opacity", 0.0, 1.0, 1.0)
        y_axis_label_color = col14.color_picker("Color", highlight_color, key="y-axis-label-color")

        col9, col10 = st.columns([5,1])
        axes_marks_opacity = col9.slider("Axes marks opacity", 0.0, 1.0, 1.0)
        axes_marks_color = col10.color_picker("Color", axes_default_color, key="axes-marks-color")

        col5, col6 = st.columns([5,1])
        legend_opacity = col5.slider("Legend opacity", 0.0, 1.0, 1.0)
        legend_text_color = col6.color_picker("Color", axes_default_color, key="legend-text-color")
        

        styling = {
            "background": background_color + ("0%x" % int(255*background_opacity))[-2:],
            "title-color": title_color + ("0%x" % int(255*title_opacity))[-2:],
            "legend-text-color": legend_text_color + ("0%x" % int(255*legend_opacity))[-2:],
            "plot-area-border": plot_area_border + ("0%x" % int(255*plot_area_border_opacity))[-2:],
            "axes-marks-color": axes_marks_color + ("0%x" % int(255*axes_marks_opacity))[-2:],
            "x-axis-label-color": x_axis_label_color + ("0%x" % int(255*x_axis_label_opacity))[-2:],
            "y-axis-label-color": y_axis_label_color + ("0%x" % int(255*y_axis_label_opacity))[-2:],
            "plot-area-border-top": "#ffffff00", 
            "plot-area-border-right": "#ffffff00", 
        }
    else:
        mpl.rcParams.update(mpl.rcParamsDefault)
        styling = None

    with st.expander("Example dict containing all available options"):
        st.write(STYLEING_DEFAULT)

st.write("# Streamlit Matplotlib SVG Demo")

st.write("## Bar Chart")

with st.expander("Code"):
    st.code('''# Store previously generated SVG in session state
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
        ''')
bar_chart_container = st.container()
value = st.slider("Multiplier", 0.1, 1.0, 1.0)

# --------- Matplotlib code ---------
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
# -----------------------------------

transitions = get_transitions(fig)
formatted_plot = svg_plot(fig, id="bar", styling=styling, transition_to=transitions)

# We want to use the svg in its previous state to transition inner elements to their new states
if st.session_state["svgb"] == "":
    last_svg = formatted_plot["svg"]
else:
    last_svg = st.session_state["svgb"]

# Update the svg in the session state
st.session_state["svgb"] = formatted_plot["svg"]

current_css = formatted_plot["css"]                           # contains current css transitions and styling
new_html = "<style>" + current_css + "</style>" + last_svg    # combine the css and LAST svg

with bar_chart_container:
    st.markdown(new_html, unsafe_allow_html=True)

with st.expander("Generated CSS template"):
    st.code(formatted_plot["css"], language="css")

# st.write("## Bar Group Chart")

st.write("## Line Plot")
line_plot_container = st.container()
line_mp_value = st.slider("Power", 0.0, 2.0, 2.0, key="line-plot")

# --------- Matplotlib code ----------
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve and estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x**(line_mp_value) + b 

fig2, ax2 = plt.subplots()
ax2.set_ylim(0, 100)

ax2.plot(x, y_est, '-')

ax2.set_xlabel('x-axis variable')
ax2.set_ylabel('y-axis variable')
ax2.set_title('Line Plot', x=0.5, y=1.05)
# -----------------------------------

line_transitions = get_transitions(fig2)
formatted_line_plot = svg_plot(fig2, id="line", styling=styling, transition_to=line_transitions)

# We want to use the svg in its previous state to transition inner elements to their new states
if st.session_state["svgl"] == "":
    last_line_svg = formatted_line_plot["svg"]
else:
    last_line_svg = st.session_state["svgl"]

# Update the svg in the session state
st.session_state["svgl"] = formatted_line_plot["svg"]

current_line_css = formatted_line_plot["css"]                           # contains current css transitions and styling
new_line_html = "<style>" + current_line_css + "</style>" + last_line_svg    # combine the css and LAST svg

with line_plot_container:
    st.markdown(new_line_html, unsafe_allow_html=True)

with st.expander("Generated CSS template"):
    st.code(formatted_line_plot["css"], language="css")

st.write("## Mixed Plot")
mix_plot_container = st.container()
mix_mp_value = st.slider("Slope", 0.0, 2.0, 2.0, key="mix-plot")

# --------- Matplotlib code ---------
v = np.linspace(0, 10, 11)
w = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve and estimate its y-values and their error.
c, d = np.polyfit(v, w, deg=1)
w_est = mix_mp_value * v + d
w_err = v.std() * np.sqrt(1/len(v) +
                          (v - v.mean())**2 / np.sum((v - v.mean())**2))

fig3, ax3 = plt.subplots()
ax3.set_ylim(0, 25)
ax3.plot(v, w_est, '-')
ax3.fill_between(v, w_est - w_err, w_est + w_err, alpha=0.2)
ax3.plot(v, w, 'o', color='tab:brown')
# -----------------------------------

mix_transitions = get_transitions(fig3)
formatted_mix_plot = svg_plot(fig3, id="mix", styling=styling, transition_to=mix_transitions)

# We want to use the svg in its previous state to transition inner elements to their new states
if st.session_state["svgm"] == "":
    last_mix_svg = formatted_mix_plot["svg"]
else:
    last_mix_svg = st.session_state["svgm"]

# Update the svg in the session state
st.session_state["svgm"] = formatted_mix_plot["svg"]

current_mix_css = formatted_mix_plot["css"]                           # contains current css transitions and styling
new_mix_html = "<style>" + current_mix_css + "</style>" + last_mix_svg    # combine the css and LAST svg

with mix_plot_container:
    st.markdown(new_mix_html, unsafe_allow_html=True)

with st.expander("Generated CSS template"):
    st.code(formatted_mix_plot["css"], language="css")