import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st
from streamlit_ydata_profiling import st_profile_report

df = pd.read_csv('Entegris_PowerCons.csv')
df.head()
pr = ProfileReport(df)
ProfileReport(pr, navbar=True)

st.title("Power Consumption Y Data Profile")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
