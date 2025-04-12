import streamlit as st
import random

from locations import locations

st.set_page_config(
    page_title = "Starter Generator",
    page_icon = "💌",
)

st.title("💌 Starter Generator")

st.write("Each input field takes either a single character name, or a comma-separated list of multiple names")

your_charas_input = st.text_input(
    "✨ Your character(s)"
)

their_charas_input = st.text_input(
    "✨ Their character(s)"
)

include_locations = st.checkbox("Would you like for the script to pick a location for you?")

if st.button("🧚🏻‍♀️✨ Let the computer work its magic!"):
    your_charas_list = [item.strip() for item in your_charas_input.split(",") if item.strip()]
    their_charas_list = [item.strip() for item in their_charas_input.split(",") if item.strip()]
    
    # we're being bad and nesting if statements
    # neither list can be empty so we wanna validate that
    if your_charas_list and their_charas_list:
        your_chara = random.choice(your_charas_list).capitalize()
        their_chara = random.choice(their_charas_list).capitalize()
        st.success(f"📜🪶✨ – {your_chara} & {their_chara}")

        if include_locations:
            random_location = random.choice(locations)
            st.info(f"Location: {random_location}")
    else:
        "Woops! Something went wrong. Check none of the boxes are empty and try again!"
