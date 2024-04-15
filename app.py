# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:48:47 2024

@author: jperezr
"""

import streamlit as st

st.title("BASE DE DATOS NACIONAL DE PENSIONES NO RECLAMADAS")

st.header("Debe tener a la mano su CURP y su NÚMERO DE SEGURIDAD SOCIAL (NSS)")

st.subheader("")
st.subheader("")
st.subheader("")


# Create an empty container
placeholder = st.empty()

actual_email = "TOGP430305MVZTCV03"
actual_password = "12345678900"

# Insert a form in the container
with placeholder.form("Acceder"):
    st.markdown("#### Intoducir:")
    email = st.text_input("CURP")
    password = st.text_input("NSS", type="password")
    submit = st.form_submit_button("Acceder")

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("CURP y NSS CORRECTOS")
    
    link = '[Puede continuar:](https://000000001-ivhfhbeaaxnnbchxfmg3hb.streamlit.app/)'
    st.markdown(link, unsafe_allow_html=True)
    
    
elif submit and email != actual_email and password != actual_password:
    st.error("DATOS INCORRECTOS")
else:
    pass
