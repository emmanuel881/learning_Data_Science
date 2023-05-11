import streamlit as sl
sl.markdown("<h1>Regestration form</h1>", unsafe_allow_html=True)
#we can use this method
form = sl.form("form 1", clear_on_submit = True)
f_name = form.text_input("First name")
sf_state = form.form_submit_button("submit")
if sf_state:
    if f_name == "":
        sl.warning("🚨🚨🚨🚨🚨🚨 invalid entry!!")
    else:
        sl.success("submitted sucessfully")

#we can also use this
with sl.form("form 2"):
    sl.text_input("last name")
    sl.form_submit_button("Submit")    
with sl.form("form 3"):
    col1, col2 = sl.columns(2)
    col1.text_input("University")
    col2.text_input("years")
    sl.text_input("Email")
    sl.text_input("Password")
    sl.text_input("confir password")
    sl.form_submit_button("Submit")    
