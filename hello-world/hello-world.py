# BASIC ELEMENT STREAMLIT

import streamlit as st
import pandas as pd

# WRITE
# untuk menampilkan sebuah output
st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40]
}))

# TEXT
st.title('Belajar Analisis Data')

st.header('Pengembangan Dashboard')

st.subheader('Pengembangan Dashboard')

st.caption('Copyright (c) 2024') # tulisan kecil / footnotes

code = """def hello()
            print("Hello, Streamlit!")"""
st.code(code, language='python') # menampilkan potorngan code

st.text('Halo, calon praktisi data masa depan.') # menampilkan teks sederhana

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right) """) # menampilkan mathematical expression yang ditulis dalam format LaTeX.


# DATA DISPLAY
import pandas as pd
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(data=df, width=500, height=150) # menampilkan data

st.table(data=df) # menampilkan data dalam bentuk static table

st.metric(label="Temperature",
          value="28 °C",
          delta="1.2 °C",
          ) # menampilkan metric beserta detail metric

st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40]
}) # menampilkan format json



# CHART
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig) # menampilkan grafik visual 
