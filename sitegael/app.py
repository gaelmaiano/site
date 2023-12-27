import requests
import streamlit as st

from PIL import Image







# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----

img_contact_form = Image.open("images/hacker.jpg")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Bonjour mon surnom est Sylas :wave:")
    st.title("Ce blog est destiné a documenter mon evolution en informatique")
    st.write(
        "Ce site est une ébauche. Il grossira avec l'ajout de contenu ulterieur"
    )
    st.write("")

# ---- WHO AM I ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who am I")
   
  
      
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Mon parcours")
        st.write(
            """Après des études en sciences humaines jusqu'au master , j ai fait un bts d'informatique et un TSAII d'automatisme et robotique
            """
        )
        st.markdown("")

        
        st.write(
            """
         Curieux de tout je compte enrichir ce site au fur et a mesure de mes trouvailles sur la toile. J envisage de faire quelques vidéos mais la premiere est encore en montage. S'il vous plait soyez patient.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/)")
    

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
   
  
      


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("me contacter!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/gintalatinamoldova@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
