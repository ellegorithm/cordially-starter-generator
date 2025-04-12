import streamlit as st
import random

st.title("💌 Starter Generator")

st.write("Each input field takes either a single character name, or a comma-separated list of multiple names")

your_charas_input = st.text_input(
    "✨ Your character(s)"
)

their_charas_input = st.text_input(
    "✨ Their character(s)"
)

if st.button("🧚🏻‍♀️✨ Let the computer work its magic!"):
    your_charas_list = [item.strip() for item in your_charas_input.split(",") if item.strip()]
    their_charas_list = [item.strip() for item in their_charas_input.split(",") if item.strip()]
    
    # we're being bad and nesting if statements
    # neither list can be empty so we wanna validate that
    if your_charas_list and their_charas_list:
        your_chara = random.choice(your_charas_list).capitalize()
        their_chara = random.choice(their_charas_list).capitalize()
        st.success(f"📜🪶✨ – {your_chara} & {their_chara}")
    else:
        "Woops! Something went wrong. Check none of the boxes are empty and try again!"
