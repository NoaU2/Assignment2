import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Noa's Homepage",
    page_icon="🎀",
)
st.write("# Welcome to Noa's Life! 😎")
st.sidebar.success("Select a topic above.")

st.markdown(
    """
    :red[Hi! I'm Noa Uritsky! Welcome to my home page] 🥰
    I'm a senior in computer science and software engineering at UW - Bothell.
    **select a page from the side bar to learn a fun fact about me :)**""" )
st.image("./me.jpg")
st.markdown(
"""## So why am I making this website? ##
For my class, obviously, but also it's fun. Also, I want to answer commonly asked questions about me
and share some fun facts.
## Why is my hair red? ##
I choose to dye my hair red for a few reasons: \n 
- **Recognizability:** a lot of people are bad with faces
- **Style:** hair color is a fun way to express my creativity
- **My Mom❤️:** as shown in ***figure 1***, my mom had red hair for **20 years**.
That's as long as I've been alive. After she stopped dyeing her hair red, I missed it so much -
I decided to dye my own hair.

"""
)

st.image("./mymama.jpg", "figure 1: my mom being cool")

