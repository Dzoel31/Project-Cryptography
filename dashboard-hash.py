""" 
    This program implements a cryptographic.
    This file is dashboard that can be used to encrypt and decrypt a message using RSA algorithm.

"""

# Import RSA library
import rsa

# Import streamlit library
import streamlit as st

st.title("RSA Cryptography")

st.header("Encrypt and Decrypt a message using RSA algorithm")

# Encrypt a message
st.subheader("Encrypt a message")

text = st.text_input("Enter a message")

# dropdown to select length of key
key_length = st.selectbox("Select length of key", [256, 512, 1024])

if text == "":
    st.warning("Please enter a message to encrypt")
    st.stop()

@st.cache_data
def generate_key(length):
    return rsa.newkeys(length)

# generate public and private key
(public_key, private_key) = generate_key(key_length)
# (public_key, private_key) = rsa.newkeys(key_length)

public_data = public_key.save_pkcs1()
st.write("Public key: ", public_data)
private_data = private_key.save_pkcs1()
st.write("Private key: ", private_data)

@st.cache_data
def encrypt_message(text, _public_key):
    return rsa.encrypt(text.encode(), _public_key)

# encrypt message
encrypted_message = encrypt_message(text, public_key)
st.write("Encrypted message: ", encrypted_message.hex())

# Decrypt a message
st.subheader("Decrypt a message")

encrypt_message_input = st.text_input("Enter encrypted message")

if encrypt_message_input == "":
    st.warning("Please enter a message to decrypt")
    st.stop()

try:
    decrypt_message = rsa.decrypt(bytes.fromhex(encrypt_message_input), private_key)
    st.write("Decrypted message: ", decrypt_message.decode())
except:
    st.warning("Please enter a valid encrypted message or check length of key")

# Download zip file containing public and private key
st.subheader("Download public and private key")

key_data = b''
key_data += public_key.save_pkcs1()
key_data += b'\n'
key_data += private_key.save_pkcs1()
# import zipfile
# with zipfile.ZipFile("keys.zip", "w") as zip:
#     zip.writestr("public.pem", public_key.save_pkcs1())
#     zip.writestr("private.pem", private_key.save_pkcs1())

# st.download_button(label="Download keys", data="keys.zip", file_name="keys.zip")
st.download_button(label="Download keys", data=key_data, file_name="keys.txt")
