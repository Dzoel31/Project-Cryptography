""" 
    This program implements a cryptographic.
    This file is dashboard that can be used to encrypt and decrypt a message using RSA algorithm.

"""

# Import RSA library
import rsa

# Import streamlit library
import streamlit as st

st.title("RSA Cryptography")
st.markdown('''
            ### [Project Cryptography](https://github.com/Dzoel31/Project-Cryptography.git)
            Kelompok 4:
            - 2210511053 - Ananda Divana
            - 2210511060 - M. Rizky Aulia
            - 2210511063 - Daffa Bagus Maulana
            - 2210511084 - Dzulfikri Adjmal
            - 2210511087 - Diaz Saputra
            ''')
            
st.header("Encrypt and Decrypt a message using RSA algorithm")

col1, col2 = st.columns(2)

with col1:
    with st.form(key="encrypt"):
        st.subheader("Encrypt a message")
        text = st.text_input("Enter a message")
        key_length = st.selectbox("Select length of key", [256, 512, 1024])
        submit = st.form_submit_button(label="Encrypt")
    
    if text == "":
        st.warning("Please enter a message to encrypt")
    
    @st.cache_data
    def generate_key(length):
        return rsa.newkeys(length)

    (public_key, private_key) = generate_key(key_length)

    @st.cache_data
    def encrypt_message(text, _public_key):
        return rsa.encrypt(text.encode(), _public_key)

# encrypt message
    if submit:
        encrypted_message = encrypt_message(text, public_key)
        st.write("Encrypted message: ", encrypted_message.hex())
        

with col2:
    with st.form(key="decrypt"):
        st.subheader("Decrypt a message")
        encrypt_message_input = st.text_input("Enter encrypted message")
        # key_length = st.selectbox("Select length of key", [256, 512, 1024])
        submit1 = st.form_submit_button(label="Decrypt")
    
    if encrypt_message_input == "":
        st.warning("Please enter a message to decrypt")
    
    try:
        decrypt_message = rsa.decrypt(bytes.fromhex(encrypt_message_input), private_key)
        st.write("Decrypted message: ", decrypt_message.decode())
        st.cache_data.clear()
    except:
        st.warning("Please enter a valid encrypted message or check length of key")

