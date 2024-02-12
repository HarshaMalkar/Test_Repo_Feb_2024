
import streamlit as st
import pandas as pd

st.write("here is my first attempt at using data to creat table")

st.write(pd.dataframe({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
}))
