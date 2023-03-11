import streamlit as st
import pandas as pd
import random

from streamlit.components.v1 import html
from customizer import customize_table

# Define the Streamlit app pages
PAGES = {
    "Home": home_page,
    "Customize Table": customize_table
}

# Define the function for the "Customize Table" page
def customize_table():
    html(customize_table())

# Display the navigation menu
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Display the selected page
page = PAGES[selection]
page()


st.set_page_config(page_title="Carlas Food Inspiration", page_icon=":fork_and_knife:", layout="wide")

# Load data from Excel file
df = pd.read_excel("food_table.xlsx")

# Define filters
herzhaft_options = ["All", "herzhaft", "süß"]
takeaway_options = ["All", "bestellen", "kochen"]
effort_options = ["All", "wenig", "mittel", "hoch"]

# Get user inputs for filters
st.write("# Carlas Food Inspiration!")
st.write("Hier muss man erst filtern:")

herzhaft = st.selectbox("herzhaft oder süß?", herzhaft_options)
if herzhaft != "All":
    df = df[df["salty"] == herzhaft]

takeaway = st.selectbox("Kochen oder Bestellen?", takeaway_options)
if takeaway != "All":
    df = df[df["takeaway"] == takeaway]
    
    if takeaway == "kochen":
        effort = st.selectbox("Wie viel Aufwand?", effort_options)
        if effort != "All":
            df = df[df["effort"] == effort]

# Suggest food
if st.button("WAS LECKRES"):
    if len(df) > 0:
        current_food = random.choice(list(df["food"]))
        st.write(f"Was Leckres: {current_food}!")
        st.write("---")
        st.button("Bäh! Ich will was leckres", key="new_suggestion")
    else:
        st.write("Leider gibt es nichts Leckeres.")

# Generate new suggestion
if "new_suggestion" in st.session_state:
    current_food = random.choice(list(df["food"]))
    st.write(f"Was Leckres: {current_food}!")
    st.write("---")
    st.button("Bäh! Ich will was leckres", key="new_suggestion")

