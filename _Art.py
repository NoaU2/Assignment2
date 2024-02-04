import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Art", page_icon="🎨")

st.markdown("# My Art #")
st.sidebar.header("My Art")
st.markdown(
    """## mapping demo first ## 
First: This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

st.write(
    """## Now my art ##
My first large painting was a :green[green skull] inspired by the haunted house I used to act at.
One of the makeup artists decided to draw a green skull on me when I was in charge of line managment."""
)
st.image("./art.jpeg")
st.write(
    """I also love crocheting and knitting, although it doesn't always look that pretty. Here is an example of a bag I made."""
)
st.image("./crochet.jpeg")
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")