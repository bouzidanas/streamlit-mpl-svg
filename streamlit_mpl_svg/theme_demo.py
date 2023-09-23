import streamlit as st
import streamlit.components.v1 as components

components.html("""
<script>
    root = window.parent.document;
    body = root.body;
    styleObj = root.documentElement.style;
    bodyProps = window.getComputedStyle(body, null);
    bgColor = bodyProps.getPropertyValue('background-color');
    color = bodyProps.getPropertyValue('color');
    font = bodyProps.getPropertyValue('font-family');
    styleObj.setProperty('--default-backgroundColor', bgColor);
    styleObj.setProperty('--default-textColor', color);
    styleObj.setProperty('--default-font', font);
                        
    cont = window.parent.document.getElementById("elim").parentElement;
    while (!cont.classList.contains("element-container")){
        cont = cont.parentElement;            
    }
    prev = cont.previousElementSibling;
    first = prev.previousElementSibling;
      
    primaryColor = window.getComputedStyle(prev.firstElementChild.firstElementChild).getPropertyValue('background-color');
    styleObj.setProperty('--default-primaryColor', primaryColor);
                
    cont.style.setProperty('display', 'none');
    prev.style.setProperty('display', 'none');
    first.style.setProperty('display', 'none');
</script>
""", 
height=0, 
width=0)
st.button("Click me", type="primary")
st.markdown("<div id='elim'><button kind='primary' data-testid='baseButton-primary'></button></div>", unsafe_allow_html=True)

st.write("My App")

st.markdown("<div style='background-color: var(--default-primaryColor);'>Hello</div>", unsafe_allow_html=True)