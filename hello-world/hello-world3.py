# BASIC LAYOUT STREAMLIT

import streamlit as st

# side-bar
st.title('Belajar Analisis Data')
with st.sidebar: # membuat side-bar

    st.text('Ini merupakan sidebar')

    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)
    # doc side bar = https://docs.streamlit.io/develop/api-reference/layout/st.sidebar


# columns
col1, col2, col3 = st.columns([2, 1, 1]) # [] untuk mengatur ukuran gambar

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")


# tabs

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")


# container

import matplotlib.pyplot as plt
import numpy as np

with st.container():
    st.write("Inside the container")

    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)
st.write("Outside the container")


# expander -> container yang dapat dibesarkan atau dikecilkan ukurannya

import matplotlib.pyplot as plt
import numpy as np
 
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum."""
    )

# doc layout dan containers https://docs.streamlit.io/develop/api-reference/layout