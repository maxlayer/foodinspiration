import streamlit as st
import pandas as pd
import random

from customizer import customize_table

st.set_page_config(page_title="Food Inspiration für Carla", page_icon=":fork_and_knife:", layout="wide")

# Load data from Excel file
df = pd.read_excel("https://github.com/maxlud/food-inspiration/blob/main/food_table.xlsx?raw=true")

# Define filters
herzhaft_options = ["All", "herzhaft", "süß"]
effort_options = ["All", "wenig", "mittel", "hoch", "bestellen"]
takeaway_options = ["All", "bestellen", "kochen"]

# Get user inputs for filters
def get_filtered_data():
    filtered_df = df.copy()
    herzhaft = st.selectbox("herzhaft oder süß?", herzhaft_options)
    if herzhaft == "herzhaft":
        filtered_df = filtered_df[filtered_df["salty"] == "herzhaft"]
    elif herzhaft == "süß":
        filtered_df = filtered_df[filtered_df["salty"] == "süß"]
    
    takeaway = st.selectbox("Kochen oder Bestellen?", takeaway_options)
    if takeaway != "All":
        filtered_df = filtered_df[filtered_df["takeaway"] == takeaway]
    
    effort = st.selectbox("How much effort?", effort_options)
    if effort != "All":
        filtered_df = filtered_df[filtered_df["effort"] == effort]
    
    return filtered_df

# Suggest food
def suggest_food():
    filtered_df = get_filtered_data()
    if st.button("WAS LECKRES"):
        if len(filtered_df) > 0:
            current_food = random.choice(list(filtered_df["food"]))
            st.write(f"Was Leckres: {current_food}!")
            st.image(filtered_df[filtered_df["food"] == current_food]["image"].values[0])
            st.button("Bäh! Ich will was leckres")
        else:
            st.write("Es gibt leider nichts leckres.")

# Define pages
def home_page():
    st.write("# Welcome to Food Inspiration!")
    st.write("Use the following filters to find your perfect food:")
    suggest_food()

def customizer_page():
    customize_table()

# Create page navigation
pages = {"Home": home_page, "Customizer": customizer_page}
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[selection]()
