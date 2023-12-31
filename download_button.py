import streamlit as st
import pandas as pd

sample_text="Some Text will be downloaded"
st.download_button('Download Text',sample_text)

with open("flower.jpg","rb") as file:
	btn=st.download_button(
		label="Download image",
		data=file,
		file_name="flower.jpg",
		mime="image/jpg"
		)

@st.cache
def convert_df(df):
	return df.to_csv().encode('utf-8')
df1=pd.read_csv('addresses.csv')
csv=convert_df(df1)
st.download_button(
	label="Download data as csv",
	data=csv,
	file_name="large_df.csv",
	mime="text/csv"
	)
