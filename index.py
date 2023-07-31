import streamlit as st

def welcome_page():
    st.title("Welcome to your favorite clinic")
    set_background('Public Opinion Research.jpg')
    st.write("Please select one of the following options:")

if __name__ == "__main__":
    welcome_page()
