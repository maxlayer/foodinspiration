import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Food Inspiration", page_icon=":fork_and_knife:", layout="wide")

# Load data from Excel file
df = pd.read_excel("food_table.xlsx")

# Define filters
herzhaft_options = ["All", "salty", "sweet"]
effort_options = ["All", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
takeaway_options = ["All", "takeaway", "cook"]

# Get user inputs for filters
st.write("# Welcome to Food Inspiration!")
st.write("Use the following filters to find your perfect food:")

herzhaft = st.selectbox("Salty or sweet?", herzhaft_options)
if herzhaft == "salty":
    df = df[df["herzhaft"] == "salty"]
elif herzhaft == "sweet":
    df = df[df["herzhaft"] == "sweet"]

effort = st.selectbox("How much effort?", effort_options)
if effort != "All":
    df = df[df["effort"] == int(effort)]

takeaway = st.selectbox("Takeaway or cook at home?", takeaway_options)
if liefern != "All":
    df = df[df["takeaway"] == takeaway]

# Suggest food
if st.button("Suggest food"):
    if len(df) > 0:
        current_food = random.choice(list(df["food"]))
        st.write(f"Try {current_food}!")
    else:
        st.write("No food found with these filters.")

# Try again button
if st.button("Bäh! Ich will was leckres"):
    st.experimental_rerun()

st.write("---")
st.write("Food data source: [www.example.com/food](www.example.com/food)")    
