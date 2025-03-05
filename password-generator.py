import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Password length", min_value=8, max_value=32, value=16)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    Password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{Password}`")

st.write("----------------")
st.write("built with ❤️ by [Tabia Nadir](https://github.com/TabiaNadir)")