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

def generate_outcome():
    outcome = random.choices(
        ["tab", "drikkevare", "turbillet"],
        weights=[7, 2, 1],
        k=1
    )[0]

    drikkevarer = ["et Tivoli postkort", "et Tivoli klistermærke", "et Tivoli badge"]
    turbilletter = ["en turbillet", "en valgfri drikkevare", "en Tivoli nøglering"]

    if outcome == "turbillet":
        emoji = random.choice(emojis)
        billet = random.choice(turbilletter)
        return [emoji] * 3, f"🎉 Du har vundet {billet}!"

    elif outcome == "drikkevare":
        emoji1 = random.choice(emojis)
        other_emojis = [e for e in emojis if e != emoji1]
        emoji2 = random.choice(other_emojis)
        pair_position = random.choice([(0, 1), (1, 2), (0, 2)])
        slots = [""] * 3
        slots[pair_position[0]] = emoji1
        slots[pair_position[1]] = emoji1
        slots[[i for i in range(3) if i not in pair_position][0]] = emoji2
        drik = random.choice(drikkevarer)
        return slots, f"🍹 Du har vundet en {drik}!"

    else:
        slots = random.sample(emojis, 3)
        return slots, "😢 Desværre, du vandt ikke denne gang."

# Start spillet
if not st.session_state.has_played:
    if st.button("🎲 Spil Mandagschancen"):
        st.session_state.slots, st.session_state.result = generate_outcome()
        st.session_state.has_played = True

# Vis slots og resultat
st.markdown(f"""
    <div style='display: flex; justify-content: center; gap: 10px;'>
        <div style='font-size: 40px;'>{st.session_state.slots[0]}</div>
        <div style='font-size: 40px;'>{st.session_state.slots[1]}</div>
        <div style='font-size: 40px;'>{st.session_state.slots[2]}</div>
    </div>
""", unsafe_allow_html=True)

if st.session_state.result:
    st.markdown("---")
    st.header(st.session_state.result)
    st.markdown("🗓️ Spil med igen næste mandag!")
