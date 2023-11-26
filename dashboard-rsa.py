""" 
    This program implements a cryptographic.
    This file is dashboard that can be used to encrypt and decrypt a message using RSA algorithm.

"""

# Import RSA library
import rsa

# Import streamlit library
import streamlit as st

st.set_page_config(page_title="RSA Cryptography", page_icon="🔐", layout='wide')

st.title("🔑 :blue[RSA Cryptography] 🔑")

st.header(":orange[Encrypt] and :orange[Decrypt] a message using RSA algorithm")

with st.expander("Apa itu RSA?"):
    st.markdown("""
                RSA adalah algoritma kriptografi asimetris pertama yang digunakan untuk enkripsi dan tanda tangan digital. 
                RSA adalah singkatan dari Rivest-Shamir-Adleman, pencipta algoritma tersebut. 
                RSA berbasis faktorisasi, yang berarti bahwa kunci publik dan kunci privatnya terkait satu sama lain melalui fungsi faktorisasi.
                """)
    
col1, col2 = st.columns(2)

with col1:
    with st.form(key="encrypt"):
        st.subheader("Encrypt a message")
        text = st.text_area("Enter a message")
        key_length = st.selectbox("Select length of key", [256, 512, 1024, 2048, 3072, 4096])

        submit = st.form_submit_button(label="Encrypt")
    
        if text == "":
            st.warning("Please enter a message to encrypt")
    
    @st.cache_data
    def generate_key(length):
        return rsa.newkeys(length, accurate=True)

    (public_key, private_key) = generate_key(key_length)

    # @st.cache_data
    def encrypt_message(text: str, _public_key):
        return rsa.encrypt(text.encode(), _public_key)
    

# encrypt message
    if submit:
        try:
            encrypted_message = encrypt_message(text, public_key)
            st.write("Encrypted message: ", encrypted_message.hex())

            private_key_copy = private_key.save_pkcs1().hex()
            st.text_area("Private key", value=private_key_copy, height=150, disabled=True)
        
        except:
            st.warning("Message to large, please enter a smaller message or use a larger key")

with col2:
    with st.form(key="decrypt"):
        st.subheader("Decrypt a message")
        encrypt_message_input = st.text_area("Enter encrypted message")
        private_key_input = st.text_area("Enter private key", disabled=False)
        submit1 = st.form_submit_button(label="Decrypt")
    
    if encrypt_message_input == "":
        st.warning("Please enter a message to decrypt")
    
    try:
        if private_key_input == "":
            st.warning("Please enter private key")
        else:
            private_key_input = rsa.PrivateKey.load_pkcs1(bytes.fromhex(private_key_input))
            decrypt_message = rsa.decrypt(bytes.fromhex(encrypt_message_input), private_key_input)
            st.write("Decrypted message: ", decrypt_message.decode())
            st.cache_data.clear()
    except:
        st.warning("Please enter a valid encrypted message or check length of key")

st.info("Setiap kali melakukan enkripsi, key akan digenerate secara otomatis. Silakan copy private key untuk melakukan dekripsi.")
st.markdown('''
            ### [Project Cryptography](https://github.com/Dzoel31/Project-Cryptography.git)
            Kelompok 4:
            - 2210511053 - Ananda Divana
            - 2210511060 - M. Rizky Aulia
            - 2210511063 - Daffa Bagus Maulana
            - 2210511084 - Dzulfikri Adjmal
            - 2210511087 - Diaz Saputra
            ''')

st.write("Group 4 Cryptograph © 2023")