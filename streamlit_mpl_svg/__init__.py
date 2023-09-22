import io
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib import font_manager

STYLEING_DEFAULT = {"background": "#ffffff", 
                    "plot-area-background": "#ffffff00", 
                    "plot-area-border": "#000000", 
                    "plot-area-border-top": "#000000", 
                    "plot-area-border-bottom": "#000000", 
                    "plot-area-border-left": "#000000", 
                    "plot-area-border-right": "#000000", 
                    "plot-area-border-width": "0.8",
                    "plot-area-text-color": "#000000",
                    "title-color": "#000000", 
                    "axes-marks-color": "#000000", 
                    "axes-marks-width": "1px", 
                    "x-axis-label-color": "#000000", 
                    "x-axis-marks-color": "#000000", 
                    "x-axis-text-color": "#000000", 
                    "x-axis-marks-width": "1px", 
                    "y-axis-label-color": "#000000", 
                    "y-axis-marks-color": "#000000", 
                    "y-axis-text-color": "#000000", 
                    "y-axis-marks-width": "1px", 
                    "plot-line-color": "#389734", 
                    "plot-line-width": "1.5", 
                    "legend-background": "#ffffff00", 
                    "legend-border-color": "#ffffff00", 
                    "legend-border-width": "1px",
                    "legend-text-color": "#000000"}
STYLEING_EXAMPLE = {"background": "#ffffff", 
                    "plot-area-background": "#ffffff00", 
                    "plot-area-border": "#000000", 
                    "plot-area-border-top": "#000000", 
                    "plot-area-border-bottom": "#000000", 
                    "plot-area-border-left": "#000000", 
                    "plot-area-border-right": "#000000", 
                    "plot-area-border-width": "0.8",
                    "plot-area-text-color": "#000000", 
                    "title-color": "#000000", 
                    "axes-marks-color": "#000000", 
                    "axes-marks-width": "1px", 
                    "x-axis-label-color": "#000000", 
                    "x-axis-marks-color": "#000000", 
                    "x-axis-text-color": "#000000", 
                    "x-axis-marks-width": "1px", 
                    "y-axis-label-color": "#000000", 
                    "y-axis-marks-color": "#000000", 
                    "y-axis-text-color": "#000000", 
                    "y-axis-marks-width": "1px", 
                    "plot-line-color": "#389734", 
                    "plot-line-width": "1.5", 
                    "legend-background": "#ffffff00", 
                    "legend-background-border-color": "#ffffff00", 
                    "legend-background-border-width": "1px",
                    "legend-text-color": "#000000"}

# Customise styling targetting main plot elements
svg_css = """/* ---------------------------------------------------- */
/* SVG area and plot area */\n
/* Matplotlib SVG */ 
svg.matplotlib-svg {
\twidth: 100%;
\theight: auto;
\tmargin-bottom: 1rem;
}
"""
svg_area_css = """
/* Matplotlib SVG background (override) */
.figure > .patch.background > path {
/*\tfill: #ffffff;*/
}
"""
plot_area_css = """
/* Plot area background (override) */
.figure > .axes > .patch.background > path.figure.axes.patch {
/*\tfill: #ffffff;*/
}
"""
plot_border_css = """
/* Plot area border */
.figure > g.axes > g.patch.border > path.figure.axes.patch {
/*\tfill: none;
\tstroke: #db1818;
\tstroke-width: 0.8;
\tstroke-linejoin: miter;
\tstroke-linecap: square;*/
}\n
"""
plot_border_override_css = """
/* Plot area border (all sides) (override) (remove contents if 
you want to style individual sides)*/
.axes > .patch.border > .figure.axes.patch {
/*\tfill: none;
\tstroke: #db1818;
\tstroke-width: 0.8;
\tstroke-linejoin: miter;
\tstroke-linecap: square;*/
}\n
"""
plot_area_text_css = """
/* Plot area text */
.axes > .text .copy {
/*\tfill: #000000;*/
}
"""
title_css = """/* Plot title */
.figure .axes > .text.last .copy {
/*\tfill: #000000;*/
}
"""
axes_css = """
/* All axes tickmarks and text */
.axes .matplotlib-axis .copy {
/*\tfill: white;
\tstroke: white;
\tstroke-width: 1px;*/
}
"""
x_axis_label_css = """
/* All x-axis text/label */
.axes .matplotlib-axis .xtick ~ .text .copy {
/*\tfill: blue;
\tstroke: blue;
\tstroke-width: 1px;*/
}
"""
x_axis_css ="""
/* All x-axis tickmarks and tickmark labels */
.axes .matplotlib-axis .xtick .copy {
/*\tfill: green;
\tstroke: green;
\tstroke-width: 3px;*/
}
"""
x_axis_text_css = """
/* All x-axis tickmark label text */
.axes .matplotlib-axis .xtick .text .copy {
/*\tfill: blue;
\tstroke: blue;
\tstroke-width: 1px;*/
}
"""
y_axis_label_css = """
/* All y-axis text/label */
.axes .matplotlib-axis .ytick ~ .text .copy {
/*\tfill: green;
\tstroke: green;
\tstroke-width: 1px;*/
}
"""
y_axis_css = """
/* All y-axis tickmarks and tickmark labels */
.axes .matplotlib-axis .ytick .copy {
/*\tfill: green;
\tstroke: green;
\tstroke-width: 1px;*/
}
"""
y_axis_text_css = """
/* All y-axis tickmark label text */
.axes .matplotlib-axis .ytick .text .copy {
/*\tfill: red;*/
}
"""

override_axes_css = """
/* Override all axes tickmarks and text */
.figure .axes .matplotlib-axis .xtick .copy, 
.axes .matplotlib-axis .ytick .copy {
/*\tfill: #000000;
\tstroke: #000000;
\tstroke-width: 1px;*/
}\n
/* ---------------------------------------------------- */
/* Individual axis elements (ticks and text characters) */
"""

plot_line_css = """
/* All plot lines */
.figure .axes > path.figure.axes.line2d {
	fill: none;
	stroke-width: 1.5;
	stroke-linecap: round;
}
"""

legend_background_css = """
/* Legend background and border */
.figure .axes > .legend > .patch.background > path {
\tfill: #ffffff00;
\tstroke: #ffffff00;
\tstroke-width: 1px;*/
}
"""
legend_text_css = """
/* Legend text */
.figure .axes > .legend > .text .copy {
/*\tfill: #ffffff00;*/
}\n
"""

def load_streamlit_default_fonts():
    font_dir = ['./fonts']
    for font in font_manager.findSystemFonts(font_dir):
        font_manager.fontManager.addfont(font)

    plt.rcParams.update({'font.family':"Source Code Pro"}) 

def fig_to_svg(fig):
    """Converts a matplotlib figure to SVG string"""
    f = io.BytesIO()
    fig.savefig(f, format="svg")
    return f.getvalue()

def get_first_parent_with_id(element):
    """Returns the first parent element with an id"""
    parent = element.parent
    while 'id' not in parent.attrs:
        parent = parent.parent
    return parent

def get_first_parent_with_class(element):
    """Returns the first parent element with a class"""
    parent = element.parent
    while 'class' not in parent.attrs:
        parent = parent.parent
    return parent

def add_class(element, class_name):
    if 'class' in element.attrs:
        element['class'] = element['class'] + " " + class_name
    else:
        element['class'] = class_name
        
def css_builder(styles={}, transition_to={}, transition=""):
    if type(styles) == dict:
        new_styles = {**STYLEING_DEFAULT}
        new_styles.update(styles)
    else:
        new_styles = {**STYLEING_DEFAULT}

    css_svg_area = svg_area_css.replace("fill: #ffffff;", "fill: " + new_styles["background"] + ";")
    css_plot_area = plot_area_css.replace("fill: #ffffff;", "fill: " + new_styles["plot-area-background"] + ";").replace("/*\t", "\t").replace("*/\n}", "\n}")
    css_plot_area_text = plot_area_text_css.replace("fill: #000000;", "fill: " + new_styles["plot-area-text-color"] + ";")
    css_plot_border = plot_border_css.replace("stroke: #db1818;", "stroke: " + new_styles["plot-area-border"] + ";")
    css_plot_border = css_plot_border.replace("stroke-width: 0.8;", "stroke-width: " + new_styles["plot-area-border-width"] + ";")

    css_title = title_css.replace("fill: #000000;", "fill: " + new_styles["title-color"] + ";")

    css_axes = axes_css.replace("fill: white;\n\tstroke: white;", "fill: " + new_styles["axes-marks-color"] + ";\n\tstroke: " + new_styles["axes-marks-color"] + ";")
    css_axes = css_axes.replace("stroke-width: 1px;", "stroke-width: " + new_styles["axes-marks-width"] + ";")
    
    css_x_axis = x_axis_css.replace("fill: green;\n\tstroke: green;", "fill: " + new_styles["x-axis-marks-color"] + ";\n\tstroke: " + new_styles["x-axis-marks-color"] + ";")
    css_x_axis = css_x_axis.replace("stroke-width: 3px;", "stroke-width: " + new_styles["x-axis-marks-width"] + ";")

    css_x_axis_label = x_axis_label_css.replace("fill: blue;\n\tstroke: blue;", "fill: " + new_styles["x-axis-label-color"] + ";\n\tstroke: " + new_styles["x-axis-label-color"] + ";")

    css_x_axis_text = x_axis_text_css.replace("fill: blue;\n\tstroke: blue;", "fill: " + new_styles["x-axis-text-color"] + ";\n\tstroke: " + new_styles["x-axis-text-color"] + ";")
    
    css_y_axis = y_axis_css.replace("fill: green;\n\tstroke: green;", "fill: " + new_styles["y-axis-marks-color"] + ";\n\tstroke: " + new_styles["y-axis-marks-color"] + ";")
    css_y_axis = css_y_axis.replace("stroke-width: 1px;", "stroke-width: " + new_styles["y-axis-marks-width"] + ";")
    
    css_y_axis_label = y_axis_label_css.replace("fill: green;\n\tstroke: green;", "fill: " + new_styles["y-axis-label-color"] + ";\n\tstroke: " + new_styles["y-axis-label-color"] + ";") 

    css_y_axis_text = y_axis_text_css.replace("fill: red;", "fill: " + new_styles["y-axis-text-color"] + ";")

    css_plot_line = plot_line_css.replace("stroke-width: 1.5;", "stroke-width: " + new_styles["plot-line-width"] + ";")

    css_legend_background = legend_background_css.replace("fill: #ffffff00;", "fill: " + new_styles["legend-background"] + ";")
    css_legend_background = css_legend_background.replace("stroke: #ffffff00;", "stroke: " + new_styles["legend-border-color"] + ";")
    css_legend_background = css_legend_background.replace("stroke-width: 1px;", "stroke-width: " + new_styles["legend-border-width"] + ";")

    css_legend_text = legend_text_css.replace("fill: #ffffff00;", "fill: " + new_styles["legend-text-color"] + ";")

    if type(styles) == dict and len(styles) > 0:
        if "background" in styles:
            css_svg_area = css_svg_area.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "plot-area-border" in styles or "plot-area-border-width" in styles:
            css_plot_border = css_plot_border.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "title-color" in styles:
            css_title = css_title.replace("/*\t", "\t").replace("*/\n}", "\n}")
        else:
            css_title = ""
        if "axes-marks-color" in styles or "axes-marks-width" in styles:
            css_axes = css_axes.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "x-axis-label-color" in styles:
            css_x_axis_label = css_x_axis_label.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "x-axis-marks-color" in styles or "x-axis-marks-width" in styles:
            css_x_axis = css_x_axis.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "x-axis-text-color" in styles:
            css_x_axis_text = css_x_axis_text.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "y-axis-label-color" in styles:
            css_y_axis_label = css_y_axis_label.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "y-axis-marks-color" in styles or "y-axis-marks-width" in styles:
            css_y_axis = css_y_axis.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "y-axis-text-color" in styles:
            css_y_axis_text = css_y_axis_text.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "plot-area-border-top" in styles:
            css_plot_border = css_plot_border + "/* Plot area border top (override) */\n.figure > g.axes > g.patch.border.top > path.figure.axes.patch {\n\tstroke: " + new_styles["plot-area-border-top"] + ";\n}\n\n"
        if "plot-area-border-bottom" in styles:
            css_plot_border = css_plot_border + "/* Plot area border bottom (override) */\n.figure > g.axes > g.patch.border.bottom > path.figure.axes.patch {\n\tstroke: " + new_styles["plot-area-border-bottom"] + ";\n}\n\n"
        if "plot-area-border-left" in styles:
            css_plot_border = css_plot_border + "/* Plot area border left (override) */\n.figure > g.axes > g.patch.border.left > path.figure.axes.patch {\n\tstroke: " + new_styles["plot-area-border-left"] + ";\n}\n\n"
        if "plot-area-border-right" in styles:
            css_plot_border = css_plot_border + "/* Plot area border right (override) */\n.figure > g.axes > g.patch.border.right > path.figure.axes.patch {\n\tstroke: " + new_styles["plot-area-border-right"] + ";\n}\n\n"
        if "plot-area-text-color" in styles:
            css_plot_area_text = css_plot_area_text.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "plot-line-color" in styles:
            if type(styles["plot-line-color"]) == str:
                css_plot_line = css_plot_line + "/* Plot line color (override) */\n.figure > .axes > .line2d:nth-child(4) > path.figure.axes.line2d {\n\tstroke: " + new_styles["plot-line-color"] + ";\n}\n\n"
            elif type(styles["plot-line-color"]) == list:
                index = 4
                for color in styles["plot-line-color"]:
                    css_plot_line = css_plot_line + "/* Individual plot line color (override) */\n.figure > .axes > .line2d:nth-child(%s) path.figure.axes.line2d {\n\tstroke: "%str(index) + color + ";\n}\n\n"
                    index += 1
        if "legend-background" in styles or "legend-border-color" in styles or "legend-border-width" in styles:
            css_legend_background = css_legend_background.replace("/*\t", "\t").replace("*/\n}", "\n}")
        if "legend-text-color" in styles:
            css_legend_text = css_legend_text.replace("/*\t", "\t").replace("*/\n}", "\n}")

    if type(transition_to) == dict and len(transition_to) > 0:
        if type(transition) is not str:
            transition = ""
        for value in transition_to.values():
            if type(value) is dict:
                css_plot_area = css_plot_area + '\n/* Transition path */\n' + value["select"] + " {\n"
                if "transition" in value:
                    css_plot_area += "\ttransition: " + value["transition"] + ";\n"
                else:
                    css_plot_area += "\ttransition: all " + transition + ";\n"
                if "d" in value:
                    css_plot_area += "\td: path('" + value["d"].replace("\n", "") + "');\n"
                if "x" in value:
                    css_plot_area += "\tx: " + value["x"] + ";\n"
                if "y" in value:
                    css_plot_area += "\ty: " + value["y"] + ";\n"
                css_plot_area += "}\n"
                
    return css_svg_area + css_plot_area + css_plot_border, css_title + css_plot_area_text + css_axes + css_x_axis_label + css_x_axis + css_x_axis_text + css_y_axis_label + css_y_axis + css_y_axis_text + override_axes_css + css_plot_line + css_legend_background + css_legend_text
    
def svg_plot(fig, id = None, styling = None, transition_to = None, transition="1s ease-in-out", append_css = ""):
    """Converts a matplotlib figure to SVG string"""
    
    transitions = {}

    svg_soup = BeautifulSoup(fig_to_svg(fig), 'lxml')

    # add class to mpl svg element
    svg_element = svg_soup.find("svg")
    add_class(svg_element, "matplotlib-svg")

    all_elements = svg_soup.find_all()

    custom_css_styles, custom_axes_css_styles = css_builder(styling, transition_to, transition)   

    # Customise styling targetting main svg elements
    css_styles = svg_css + custom_css_styles

    # Customise styling targetting axes elements    
    axes_css_styles = custom_axes_css_styles

    # Add classes to all elements that have an id and are not in defs.
    # Class names are based on the element ids.
    for element in all_elements:
        if 'id' in element.attrs:
            add_class(element, element['id'].split("_")[0].replace(".", "-"))
            paths = element.find_all("path")
            for path in paths:
                if path.parent.name != "defs":
                    add_class(path, element['id'].split("_")[0].replace(".", "-"))
            
    paths = svg_soup.find_all("path")
    path_count = 0

    # Add special classes to paths that are in defs.
    for path in paths:
        if path.parent.name != "defs":
            add_class(path, "path-" + str(path_count))
            if "style" in path.attrs:
                css_styles += '.' + '.'.join(path['class'].split()) + ' {\n\t' +  path['style'].replace('; ', ';\n\t') + ';\n}\n\n'
                path['style'] = ""
            else:
                css_styles += '.' + '.'.join(path['class'].split()) + ' {\n}\n\n'
            path_count += 1

    css_styles += axes_css_styles

    poly_collections = svg_soup.select(".figure > .axes > .PolyCollection")
    poly_index = 1
    for poly_collection in poly_collections:
        temp_poly_dict = {}
        if "id" in poly_collection.attrs:
            temp_poly_dict["select"] = "#" + poly_collection["id"] + " > path"
            if "d" in poly_collection.path.attrs:
                temp_poly_dict["d"] = poly_collection.path['d']
            if "x" in poly_collection.path.attrs:
                temp_poly_dict["x"] = poly_collection.path["x"]
            if "y" in poly_collection.path.attrs:
                temp_poly_dict["y"] = poly_collection.path["y"]
            transitions["PolyCollection-" + str(poly_index)] = temp_poly_dict
        else:
            transitions["PolyCollection-" + str(poly_index)] = None
        poly_index += 1

    lines = svg_soup.select(".figure > .axes > .line2d")
    line_index = 1
    for line in lines:
        add_class(line, "transition-line-" + str(line_index))
        if line.path['d'] != "":
            transitions["transition-line-" + str(line_index)] = {"select": ".transition-line-" + str(line_index) + " > path", "d": line.path['d']}
        else:
            transitions["transition-line-" + str(line_index)] = None
        
        line_index += 1

    border_paths = svg_soup.select(".figure > .axes > .patch")
    border_index = 0
    for border_path in border_paths[-4:]:
        if border_index == 0:
            add_class(border_path, "border left")
        elif border_index == 1:
            add_class(border_path, "border right")
        elif border_index == 2:
            add_class(border_path, "border bottom")
        elif border_index == 3:
            add_class(border_path, "border top")
        border_index += 1
    
    add_class(border_paths[0], "background")

    if len(border_paths) > 5:
        patch_index = 1
        for border_path in border_paths[1:-4]:
            add_class(border_path, "content transition-paths-" + str(patch_index))
            if border_path.path['d'] != "":
                transitions["transition-paths-" + str(patch_index)] = {"select": ".transition-paths-" + str(patch_index) + " > path", "d": border_path.path['d']}
            else:
                transitions["transition-paths-" + str(patch_index)] = None
            patch_index += 1
    
    svg_background_patch = svg_soup.select(".figure > .patch:first-child")
    if len(svg_background_patch) > 0:
        add_class(svg_background_patch[0], "background")

    legend_background_patch = svg_soup.select(".figure > .axes > .legend > .patch:first-child")
    if len(legend_background_patch) > 0:
        add_class(legend_background_patch[0], "background")

    plot_area_text = svg_soup.select(".figure > .axes > .text")
    if len(plot_area_text) > 0:
        add_class(plot_area_text[-1], "last")

    use_counts = []
    use_parent_classes = []
    uses_inside = svg_soup.find_all("use")

    for use_element in uses_inside:
        parent_class = get_first_parent_with_class(use_element)['class'].split()[-1]
        if parent_class not in use_parent_classes:
            use_parent_classes.append(parent_class)
            use_counts.append(0)
        else:
            use_counts[use_parent_classes.index(parent_class)] += 1

        use_count = use_counts[use_parent_classes.index(parent_class)]
        add_class(use_element, "copy " + parent_class + " copy-" + str(use_count))
        if "style" in use_element.attrs:
            css_styles += '.' + parent_class + '.copy-' + str(use_count) + ' {\n\t' + use_element['style'].replace('; ', ';\n\t') + ';\n}\n\n'
            use_element['style'] = ""
        else:
            css_styles += '.' + parent_class + '.copy-' + str(use_count) + ' {\n}\n\n'
    
    line_index = 1
    for line in lines:       
        copies = line.select(".copy")
        for copy_index in range(len(copies)):
            copy = copies[copy_index]
            if "x" in copy.attrs and "y" in copy.attrs:
                transitions["transition-line-" + str(line_index) + "-copy-" + str(copy_index)] = {"select": '.' + '.'.join(copy["class"].split())}
                if copy['x'] != "":
                    transitions["transition-line-" + str(line_index) + "-copy-" + str(copy_index)]["x"] = copy['x']
                if copy['y'] != "":
                    transitions["transition-line-" + str(line_index) + "-copy-" + str(copy_index)]["y"] = copy['y']
            else:
                transitions["transition-line-" + str(line_index) + "-copy-" + str(copy_index)] = None
        line_index += 1
    
    path_styles_in_defs ="""/* ---------------------------------------------------- */
    /* Original paths of copies */\n\n"""
    class_count = 0
    def_elem_dict = {}
    defs_elements = svg_soup.find_all("defs")
    for defs in defs_elements:
        elements = defs.find_all()
        for element in elements:
            if 'id' in element.attrs:
                def_elem_dict[element['id']] = element

                if "class" in element.attrs:
                    element['class'] = "def-" + element.name + "-" + str(class_count)
                    class_count += 1
                    if "style" in element.attrs:
                        path_styles_in_defs += '.' + '.'.join(element['class'].split()) + ' {\n\t/*' + element['style'].replace('; ', ';\n\t') + ';*/\n}\n\n'
                        element['style'] = ""
                    else:
                        path_styles_in_defs += '.' + '.'.join(element['class'].split()) + ' {\n}\n\n'        

    if id is not None:
        svg_element['id'] = id
        combined_css = css_styles + path_styles_in_defs
        combined_css = combined_css.replace("\n.", "\n#" + id + " .")
    else:
        combined_css = css_styles + path_styles_in_defs

    final_svg = svg_soup.find("svg")
    html_style = "<style>\n" + combined_css + append_css + "\n</style>"
    return {"html": html_style + final_svg.prettify(), "svg": final_svg.prettify(), "css": combined_css + append_css, "transitions": transitions}

def get_transitions(fig):
    transitions = {}
    svg_soup = BeautifulSoup(fig_to_svg(fig), 'lxml')
    all_elements = svg_soup.find_all()

    # Add classes to all elements that have an id and are not in defs.
    # Class names are based on the element ids.
    for element in all_elements:
        if 'id' in element.attrs:
            add_class(element, element['id'].split("_")[0].replace(".", "-"))
            paths = element.find_all("path")
            for path in paths:
                if path.parent.name != "defs":
                    add_class(path, element['id'].split("_")[0].replace(".", "-"))

    poly_collections = svg_soup.select(".figure > .axes > .PolyCollection")
    poly_index = 1
    for poly_collection in poly_collections:
        temp_poly_dict = {}
        if "id" in poly_collection.attrs:
            temp_poly_dict["select"] = "#" + poly_collection["id"] + " > path"
            if "d" in poly_collection.path.attrs:
                temp_poly_dict["d"] = poly_collection.path['d']
            if "x" in poly_collection.path.attrs:
                temp_poly_dict["x"] = poly_collection.path["x"]
            if "y" in poly_collection.path.attrs:
                temp_poly_dict["y"] = poly_collection.path["y"]
            transitions["PolyCollection-" + str(poly_index)] = temp_poly_dict
        else:
            transitions["PolyCollection-" + str(poly_index)] = None
        poly_index += 1

    lines = svg_soup.select(".figure > .axes > .line2d")
    line_index = 1
    for line in lines:
        add_class(line, "transition-line-" + str(line_index))
        if line.path['d'] != "":
            transitions["transition-line-" + str(line_index)] = {"select": ".transition-line-" + str(line_index) + " > path", "d": line.path['d']}
        else:
            transitions["transition-line-" + str(line_index)] = None
        line_index += 1

    border_paths = svg_soup.select(".figure > .axes > .patch")
    if len(border_paths) > 5:
        patch_index = 1
        for border_path in border_paths[1:-4]:
            if border_path.path['d'] != "":
                transitions["transition-paths-" + str(patch_index)] = {"select": ".transition-paths-" + str(patch_index) + " > path", "d": border_path.path['d']}
            else:
                transitions["transition-paths-" + str(patch_index)] = None
            patch_index += 1

    use_counts = []
    use_parent_classes = []
    uses_inside = svg_soup.find_all("use")

    for use_element in uses_inside:
        parent_class = get_first_parent_with_class(use_element)['class'].split()[-1]
        if parent_class not in use_parent_classes:
            use_parent_classes.append(parent_class)
            use_counts.append(0)
        else:
            use_counts[use_parent_classes.index(parent_class)] += 1
        use_count = use_counts[use_parent_classes.index(parent_class)]
        add_class(use_element, "copy " + parent_class + " copy-" + str(use_count))

    line_index = 1
    for line in lines:       
        copies = line.select(".copy")
        for copy_index in range(len(copies)):
            copy = copies[copy_index]
            if "x" in copy.attrs and "y" in copy.attrs:
                transitions["transition-line-" + str(line_index) + "-copy-" + str(copy_index)] = {"select": '.' + '.'.join(copy["class"].split())}
                if copy['x'] != "":
                    transitions["transition-line-" + str(line_index) + "-copy-" + str(copy_index)]["x"] = copy['x']
                if copy['y'] != "":
                    transitions["transition-line-" + str(line_index) + "-copy-" + str(copy_index)]["y"] = copy['y']
            else:
                transitions["transition-line-" + str(line_index) + "-copy-" + str(copy_index)] = None
        line_index += 1
    
    return transitions