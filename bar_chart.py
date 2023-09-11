import streamlit as st
import numpy as np
import pandas as pd

chart_data=pd.DataFrame(np.random.randn(20,3),
		columns=['a','b','c'])

st.bar_chart(chart_data)