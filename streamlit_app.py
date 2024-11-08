import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st
from streamlit_ydata_profiling import st_profile_report

df = pd.read_csv('air_comp_data_new.csv')
pr = ProfileReport(df, minimal=True, orange_mode=True, explorative=True)
st_profile_report(pr, navbar=True)

st.title("Power Consumption Y Data Profile")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
