import streamlit as st
import numpy as np
import pandas as pd

df=pd.DataFrame(np.random.randn(10,5),
		columns=('col %d' % i for i in range(5)))

st.table(df)