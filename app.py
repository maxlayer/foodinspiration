import streamlit as st
import pandas as pd
import random

# Load data from Excel file
food_table = pd.read_excel('food_table.xlsx')

# Sidebar filters
herzhaft = st.sidebar.selectbox("Salty or sweet?", ["Any", "Salty", "Sweet"])
dauer = st.sidebar.slider("Effort", 1, 9, (1, 9), 1)
liefern = st.sidebar.selectbox("Takeaway or cook at home?", ["Any", "Takeaway", "Cook at home"])

# Apply filters
if herzhaft != "Any":
    filtered_food_table = food_table.loc[food_table["herzhaft"] == herzhaft]
else:
    filtered_food_table = food_table.copy()

filtered_food_table = filtered_food_table.loc[(filtered_food_table["dauer"] >= dauer[0]) & (filtered_food_table["dauer"] <= dauer[1])]

if liefern != "Any":
    filtered_food_table = filtered_food_table.loc[filtered_food_table["liefern"] == liefern]

# Display a random food
if not filtered_food_table.empty:
    current_food = random.choice(filtered_food_table["essen"])
    st.write("How about", current_food, "?")
else:
    st.write("No food found with the selected filters.")

# Reshuffle button
if st.button("Reshuffle"):
    if not filtered_food_table.empty:
        current_food = random.choice(filtered_food_table["essen"])
        st.write("How about", current_food, "?")
    else:
        st.write("No food found with the selected filters.")
