
import streamlit as st
import random
from PIL import Image
import os

st.set_page_config(page_title="Mandagschancen 🎰", page_icon="🎠")
st.title("🎰 Mandagschancen - Prøv lykken!")

emojis = ["🎢", "🎠", "🎡", "🎯", "🍿", "🎟️"]

if "slots" not in st.session_state:
    st.session_state.slots = ["❔", "❔", "❔"]
if "result" not in st.session_state:
    st.session_state.result = ""
if "has_played" not in st.session_state:
    st.session_state.has_played = False

# Vis Tivoli-logo øverst
if os.path.exists("tivoli_logo2.png"):
    img = Image.open("tivoli_logo2.png")
    width = 200
    height = int((width / img.width) * img.height)
    col = st.columns([1, 3, 1])[1]
    with col:
        st.image(img.resize((width, height)), use_container_width=False)

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

# Vis slots i mobilvenlig flexbox
st.markdown("""
    <div style='display: flex; justify-content: center; gap: 10px;'>
        <div style='font-size: 40px;'>""" + st.session_state.slots[0] + """</div>
        <div style='font-size: 40px;'>""" + st.session_state.slots[1] + """</div>
        <div style='font-size: 40px;'>""" + st.session_state.slots[2] + """</div>
    </div>
""", unsafe_allow_html=True)

# Vis resultat
st.markdown("🗓️ Spil med igen næste mandag!")
