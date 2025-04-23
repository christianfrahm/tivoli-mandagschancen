
import streamlit as st
import random
import os
from PIL import Image

st.set_page_config(page_title="Mandagschancen 🎰", page_icon="🎠")

# Tilføj Tivoli-logo øverst
if os.path.exists("tivoli_logo2.png"):
    img = Image.open("tivoli_logo2.png")
    st.image(img, width=200)

st.title("🎰 Mandagschancen - Prøv lykken!")

emojis = ["🎢", "🎠", "🎡", "🎯", "🍿", "🎟️"]

if "slots" not in st.session_state:
    st.session_state.slots = ["❔", "❔", "❔"]
if "result" not in st.session_state:
    st.session_state.result = ""
if "has_played" not in st.session_state:
    st.session_state.has_played = False

# Start spillet - kun vis knappen hvis man ikke allerede har spillet
if not st.session_state.has_played:
    if st.button("🎲 Spil Mandagschancen"):
        st.session_state.slots = [random.choice(emojis) for _ in range(3)]
        final = st.session_state.slots
        if final[0] == final[1] == final[2]:
            st.session_state.result = "🎉 Du har vundet en turbillet!"
        elif final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
            st.session_state.result = "🍹 Du har vundet en valgfri drikkevare!"
        else:
            st.session_state.result = "😢 Desværre, du vandt ikke denne gang."
        st.session_state.has_played = True

# Vis slots og resultat i mobilvenlig flexbox layout
st.markdown("""
    <div style='display: flex; justify-content: center; gap: 10px;'>
        <div style='font-size: 40px;'>""" + st.session_state.slots[0] + """</div>
        <div style='font-size: 40px;'>""" + st.session_state.slots[1] + """</div>
        <div style='font-size: 40px;'>""" + st.session_state.slots[2] + """</div>
    </div>
""", unsafe_allow_html=True)

if st.session_state.result:
    st.markdown("---")
    st.header(st.session_state.result)
    st.markdown("🗓️ Spil med igen næste mandag!")
