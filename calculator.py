import streamlit as st
import pandas as pd
import numpy as np
from sympy import symbols, solve

textboxlabel = " "

colA, colB, colC = st.columns([2,4,2])

colB.title('Calculator')

col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 2])

if 'operant' not in st.session_state:
    st.session_state.operant = ""
if 'txt' not in st.session_state:
    st.session_state.txt = "0"

def numpad(num=""):
    if st.session_state.txt == "0":
        st.session_state.txt = num
    else:
        st.session_state.txt += num
    st.session_state.operant = ""
    textboxlabel = " "

def operant(opr=""):
    if st.session_state.operant != "":
        st.session_state.txt = st.session_state.txt[:-1] + opr
    else:
        st.session_state.txt += opr
    st.session_state.operant = opr
    textboxlabel = " "

if col2.button("C", type="primary"):
    st.session_state.txt = "0"
    st.session_state.operant = ""
if col2.button("7"):
    numpad("7")
if col3.button("✕"):
    operant("*")
if col3.button("8"):
    numpad("8")
if col4.button("÷"):
    operant("/")
if col4.button("9"):
    numpad("9")
if col5.button("＋"):
    operant("+")
if col5.button("--"):
    operant("-")

colB.text_area(textboxlabel, st.session_state.txt)
