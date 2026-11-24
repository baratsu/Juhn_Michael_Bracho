import streamlit as st

st.header("Juhn Michael Bracho")

st.write("Welcome to my Streamlit Web Application!")

st.subheader("About Me")
st.write("""Hello!I am Juhn Michael Bracho. This is my first streamlit web application.""")

st.subheader("Interactive Section")

name = st.text_input("Enter your name:")
if name:
	st.success(f"Hello,{name}! Welcome to my application.")

st.write("---")
st.caption("Created by Juhn Michael Bracho")