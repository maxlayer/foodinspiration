import pandas as pd
import streamlit as st
import random

# Load data from Excel file
food_table = pd.read_excel("food_table.xlsx")

# Sidebar filters
st.sidebar.header("Filters")
salty_sweet = st.sidebar.radio("Salty or sweet?", ("All", "Salty", "Sweet"))
effort = st.sidebar.slider("Effort", 1, 9, (1, 9))
takeaway_cookathome = st.sidebar.radio("Takeaway or cook at home?", ("All", "Takeaway", "Cook at home"))

# Filter the food table
filtered_food_table = food_table.copy()
if salty_sweet != "All":
    filtered_food_table = filtered_food_table[filtered_food_table["herzhaft"] == salty_sweet.lower()]
filtered_food_table = filtered_food_table[(filtered_food_table["dauer"] >= effort[0]) & (filtered_food_table["dauer"] <= effort[1])]
if takeaway_cookathome != "All":
    filtered_food_table = filtered_food_table[filtered_food_table["liefern"] == takeaway_cookathome.lower()]

# Shuffle the filtered food table and display a random food
shuffled_food = random.sample(list(filtered_food_table["essen"]), len(filtered_food_table))
current_food_idx = st.empty()
if st.button("Reshuffle"):
    shuffled_food = random.sample(list(filtered_food_table["essen"]), len(filtered_food_table))
current_food_idx.markdown(shuffled_food[0], True)
