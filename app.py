import streamlit as st
import pandas as pd
import random

# Load data
@st.cache
def load_data(file_path):
    return pd.read_excel(file_path)

food_table = load_data('food_table.xlsx')

# Filters
herzhaft_filter = st.sidebar.radio("Salty or sweet?", ("Salty", "Sweet", "Any"))
dauer_filter = st.sidebar.slider("Effort level (1-9)", 1, 9, (1, 9))
liefern_filter = st.sidebar.checkbox("Only delivery/takeaway?")

# Apply filters
filtered_food_table = food_table.copy()
if herzhaft_filter != "Any":
    filtered_food_table = filtered_food_table[filtered_food_table["herzhaft"] == herzhaft_filter.lower()]
if dauer_filter != (1, 9):
    filtered_food_table = filtered_food_table[filtered_food_table["dauer"].between(*dauer_filter)]
if liefern_filter:
    filtered_food_table = filtered_food_table[filtered_food_table["liefern"] == "ja"]

# Shuffle
if st.button("Reshuffle"):
    current_food = random.choice(filtered_food_table["essen"])
else:
    current_food = st.session_state.get("current_food")
    if not current_food or current_food not in filtered_food_table["essen"].values:
        current_food = random.choice(filtered_food_table["essen"])
    st.session_state.current_food = current_food

# Display
st.write("# What's for food today?")
st.write(f"## {current_food}")


