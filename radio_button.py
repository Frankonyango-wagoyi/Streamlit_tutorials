import streamlit as st

genre=st.radio(
	"Whats your favourite movie genre?",
	('Comedy','Drama','Documentary'))
if genre =='Comedy':
	st.write('You selected Comedy.')
else:
	st.write('You did not select comedy.')