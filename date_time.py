import streamlit as st
import datetime 

d=st.date_input('When is your birthday?',
		datetime.date(2002,8,16))
st.write("Your birthday is:",d)