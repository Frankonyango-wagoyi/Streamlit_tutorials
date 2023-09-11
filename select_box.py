import streamlit as st

option=st.selectbox(
	'How would you like to be contacted?',
	{'Email','Home Phone','Mobile Phone'})
st.write('You selected',option)