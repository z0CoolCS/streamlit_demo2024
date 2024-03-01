import streamlit as st

import numpy as np
import pandas as pd


st.markdown('# Welcome to my app')

line = st.slider('Selecciona valor', 0, 10, 3)

if st.button('click me'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    st.write('Further clicks are not visible but are executed')

def get_data():
    return pd.DataFrame(
            np.random.randn(3, 3),
            columns=['a', 'b', 'c'])

@st.cache_data
def get_cached_data():
    return get_data()

columns = st.columns(2)

columns[0].write("Uncached dataframe")
columns[0].write(get_data())

columns[1].write("Cached dataframe")
columns[1].write(get_cached_data())
