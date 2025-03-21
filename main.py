import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx
import time
from threading import Thread
st.title("hello world")
st.write("welcome to streamlit app ....")

if st.button("say hello"):
    st.text("hello, streamlit...")
name=st.text_input("please enter your name !..")
if name:
    st.write("{}".format(name))
if st.file_uploader("please upload a file ",type=["abc.txt","def.csv"]):
    st.write("thanks for uploading a file..")










