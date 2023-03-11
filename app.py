import streamlit as st
import pandas as pd
import random

# Load the food table from a CSV file
food_table = pd.read_excel('food_table.xlsx')

# Define the filter options
takeaway_options = ['All', 'Takeaway', 'Cook at home']
sweet_salty_options = ['All', 'Sweet', 'Salty']

# Create the filter widgets
takeaway_filter = st.sidebar.selectbox('Takeaway or cook at home?', takeaway_options)
sweet_salty_filter = st.sidebar.selectbox('Sweet or salty?', sweet_salty_options)

# Apply the filters to the food table
if takeaway_filter != 'All':
    food_table = food_table[food_table['liefern'] == takeaway_filter]
if sweet_salty_filter != 'All':
    food_table = food_table[food_table['herzhaft'] == sweet_salty_filter]

# Shuffle the remaining food and select one
if len(food_table) > 0:
    shuffled_food = random.sample(list(food_table['essen']), len(food_table))
    selected_food = shuffled_food[0]
    st.write('Hey Carla, hier ist was leckres: ', selected_food, '?')
else:
    st.write('Es gibt einfach nichts leckres.')

