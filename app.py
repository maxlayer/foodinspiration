import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Food Inspiration", page_icon=":fork_and_knife:", layout="wide")

# Load data from Excel file
df = pd.read_excel("food_table.xlsx")

# Define filters
herzhaft_options = ["All", "Herzhaft", "Süße"]
dauer_options = ["All", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
liefern_options = ["All", "Okay", "Lieber nicht"]

# Get user inputs for filters
st.write("# Welcome to Food Inspiration!")
st.write("Use the following filters to find your perfect food:")

herzhaft = st.selectbox("Salty or sweet?", herzhaft_options)
if herzhaft == "Salty":
    df = df[df["herzhaft"] == "Herzhaft"]
elif herzhaft == "Sweet":
    df = df[df["herzhaft"] == "Süß"]

dauer = st.selectbox("How much effort?", dauer_options)
if dauer != "All":
    df = df[df["dauer"] == int(dauer)]

liefern = st.selectbox("Takeaway or cook at home?", liefern_options)
if liefern != "All":
    df = df[df["liefern"] == "Okay"]

# Suggest food
if st.button("Suggest food"):
    if len(df) > 0:
        current_food = random.choice(list(df["essen"]))
        st.write(f"Try {current_food}!")
    else:
        st.write("No food found with these filters.")

# Try again button
if st.button("Bäh! Was Leckres"):
    st.experimental_rerun()

st.write("---")
st.write("Food data source: [www.example.com/food](www.example.com/food)")    
