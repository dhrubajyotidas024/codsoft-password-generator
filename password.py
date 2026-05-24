import streamlit as st
import random
import string

# Title
st.title("🔐 Password Generator")

# User Input
length = st.number_input(
    "Enter Password Length",
    min_value=1,
    max_value=100,
    value=8
)

# Generate Password Function
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

# Button
if st.button("Generate Password"):
    password = generate_password(length)

    st.success("Password Generated Successfully!")
    st.code(password, language="text")