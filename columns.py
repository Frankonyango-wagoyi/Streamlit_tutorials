import streamlit as st

col1,col2,col3=st.columns(3)

with col1:
	st.header("This is column1")
	st.write("Some text inside column1")
with col2:
	st.header("This is column2")
	st.write("Some text inside column2")
with col3:
	st.header("This is column3")
	st.write("Some text inside column3")