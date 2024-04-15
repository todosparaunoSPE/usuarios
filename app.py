# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:48:47 2024

@author: jperezr
"""

import streamlit as st

st.title("BASE DE DATOS NACIONAL DE PENSIONES NO RECLAMADAS")

st.header("")

st.subheader("")
st.subheader("")
st.subheader("")


# Create an empty container
placeholder = st.empty()

actual_email = ['TOGP430305MVZTCV03','SAAA411108MVZTCV04','TOGP430305MVZTCV05']
actual_password = ['12345678900','12345678911','12345678922']




# Insert a form in the container
with placeholder.form("Acceder"):
    st.markdown("#### Intoducir:")
    email = st.text_input("CURP")
    password = st.text_input("NSS", type="password")
    submit = st.form_submit_button("Acceder")
    
    
    
 
    

if email == actual_email[0] and password == actual_password[0]:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("CURP y NSS CORRECTOS")
    
    link = '[Puede continuar:](https://000000001-ivhfhbeaaxnnbchxfmg3hb.streamlit.app/)'
    st.markdown(link, unsafe_allow_html=True)
    
    
elif email == actual_email[1] and password == actual_password[1]:
    


#if email == actual_email[1] and password == actual_password[1]:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("CURP y NSS CORRECTOS")
    
    link = '[Puede continuar:](https://000000002-oex4oba9ajxxevgn2ctgde.streamlit.app/)'
    st.markdown(link, unsafe_allow_html=True)
    
    
#elif submit and email != actual_email[1] and password != actual_password[1]:
#    st.error("DATOS INCORRECTOS")
#else:
#     pass

elif email == actual_email[2] and password == actual_password[2]:
    #pass 


#if email == actual_email[2] and password == actual_password[2]:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("CURP y NSS CORRECTOS")
    
    link = '[Puede continuar:](https://www.gob.mx/pensionissste)'
    st.markdown(link, unsafe_allow_html=True)
    
    
elif submit and email != actual_email[0] and password != actual_password[0] and email != actual_email[1] and password != actual_password[1] and email != actual_email[2] and password != actual_password[2]:
#    st.error("DATOS INCORRECTOS")
   st.error("DATOS INCORRECTOS")
    #pass
    
