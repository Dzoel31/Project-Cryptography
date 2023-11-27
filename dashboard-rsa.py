""" 
    This program implements a cryptographic.
    This file is dashboard that can be used to encrypt and decrypt a message using RSA algorithm.

"""
# Import RSA library
import rsa

# Import streamlit library
import streamlit as st

st.set_page_config(page_title="RSA Cryptography", page_icon="🔐", layout='wide')

def welcome_page():
    st.title("✨ Welcome to RSA Cryptography 🎉")
    st.markdown(
        """
        Halo!, selamat datang di aplikasi kami. Aplikasi ini dapat digunakan untuk melakukan enkripsi dan dekripsi pesan menggunakan algoritma RSA.

        **👈Silakan pilih menu di sebelah kiri** untuk melakukan enkripsi dan dekripsi pesan.

        ### Info lebih lanjut cek link berikut:
        - [RSA Cryptography](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) wikipedia
        - [RSA Cryptography](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/) geeksforgeeks
        - [Source Code](https://github.com/Dzoel31/Project-Cryptography) GitHub
        """
            )


def encrypt_page():

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
            key_length = st.selectbox("Select length of key", [256, 512, 1024, 2048, 3072, 4096])
            text = st.text_area("Enter a message")

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
                st.warning("Message to large, please enter a smaller message or use a larger key. Key with Lenght {} can only encrypt {} characters".format(key_length, key_length//8 - 11))

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

    st.write("Group 4 Cryptograph © 2023")

def docs_page():
    st.title("📖 Documentation 📖")
    st.markdown(
        """
        ### Documentation
        - [Streamlit](https://docs.streamlit.io/en/stable/)
        - [RSA](https://stuvel.eu/python-rsa-doc/)
        - [Source Code](https://github.com/Dzoel31/Project-Cryptography)

        ### How to use (run locally)

        1. Clone this repository

            ```bash
            git clone https://github.com/Dzoel31/Project-Cryptography.git
            ```
            note: You must have git installed on your computer or you can download zip file from [this repository](https://github.com/Dzoel31/Project-Cryptography).
        2. Install requirements
            This program using rsa and streamlit library. You can install it using pip command.

            ```bash
            pip install rsa
            pip install streamlit
            ```

            or you can install it using requirements.txt
                
            ```bash
            pip install -r requirements.txt
            ```

        3. Run the program
            ```bash
            streamlit run dashboard-rsa.py
            ```
        4. Open your browser and go to http://localhost:8501
        5. Enjoy!
        """)

def about_us():
    st.title("👨‍💻 About Us 👨‍💻")
    st.markdown(
        """
        ### About Us
        Kelompok 4:
        - 2210511053 - Ananda Divana
        - 2210511060 - M. Rizky Aulia
        - 2210511063 - Daffa Bagus Maulana
        - 2210511084 - Dzulfikri Adjmal
        - 2210511087 - Diaz Saputra
        """
        )

page_name = {
    "Welcome Page": welcome_page,
    "Encrypt Page": encrypt_page,
    "Documentation": docs_page,
    "About Us": about_us
}

page_select = st.sidebar.selectbox("Select page", list(page_name.keys()))
page_name[page_select]()
