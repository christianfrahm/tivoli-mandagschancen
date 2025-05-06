import streamlit as st
import random
import os
from PIL import Image

st.set_page_config(page_title="Monday Chance 🎰", page_icon="🎠")

# Add Tivoli logo at the top
if os.path.exists("tivoli_logo2.png"):
    img = Image.open("tivoli_logo2.png")
    st.image(img, width=200)

st.title("🎰 Monday Chance - Try Your Luck!")

emojis = ["🎢", "🎠", "🎡", "🎯", "🍿", "🎟️"]

if "slots" not in st.session_state:
    st.session_state.slots = ["❔", "❔", "❔"]
if "result" not in st.session_state:
    st.session_state.result = ""
if "has_played" not in st.session_state:
    st.session_state.has_played = False

def generate_outcome():
    outcome = random.choices(
        ["lose", "small_prize", "big_prize"],
        weights=[7, 2, 1],
        k=1
    )[0]

    small_prizes = ["a Tivoli postcard", "a Tivoli sticker", "a Tivoli badge"]
    big_prizes = ["a ride ticket", "a free beverage of your choice", "a Tivoli keychain"]

    if outcome == "big_prize":
        emoji = random.choice(emojis)
        prize = random.choice(big_prizes)
        return [emoji] * 3, f"🎉 Congratulations! You've won {prize}!"

    elif outcome == "small_prize":
        emoji1 = random.choice(emojis)
        other_emojis = [e for e in emojis if e != emoji1]
        emoji2 = random.choice(other_emojis)
        pair_position = random.choice([(0, 1), (1, 2), (0, 2)])
        slots = [""] * 3
        slots[pair_position[0]] = emoji1
        slots[pair_position[1]] = emoji1
        slots[[i for i in range(3) if i not in pair_position][0]] = emoji2
        prize = random.choice(small_prizes)
        return slots, f"🍹 You've won {prize}!"

    else:
        slots = random.sample(emojis, 3)
        return slots, "😢 Sorry, no prize this time."

# Start the game
if not st.session_state.has_played:
    if st.button("🎲 Play Monday Chance"):
        st.session_state.slots, st.session_state.result = generate_outcome()
        st.session_state.has_played = True

# Display the slots and result
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
    st.markdown("🗓️ Come back and play again next Monday!")
