# BASIC WIDGET STREAMLIT

import streamlit as st

# 1. INPUT WIDGET

# text-input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

# text-area
text = st.text_area('Feedback')
st.write('Feedback', text)

# number-input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

# date-input
import datetime
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1990, 1, 1))
st.write('Tanggal lahir: ', date)

# file-uploader
import pandas as pd
uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# camera-input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)


# 2. BUTTON WIDGET

# button
if st.button('Say hello'):
    st.write('Hello there')

# checkbox
agree = st.checkbox('I agree')
if agree:
    st.write('Welcome to MyApp')

# radio-button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

# select-box
genre2 = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
)

# multi-select
genre3 = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100)
)
st.write("Values: ", values)

# info lebih lanjut widget cek dokumentasinya:
# https://docs.streamlit.io/develop/api-reference/widgets