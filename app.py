import streamlit as st
import pandas as pd
import random

# Define food table
food_table = pd.DataFrame({
    'food': ['Tortellini mit Käse Sahne Soße', 'Nutella Brot', 'Pizza bestellen', 'Vegetarisches Sushi', 'Ein Spiegelei', 'Tomate Mozarella Salat', 'Käsebrot', 'Sushi selber machen', 'Pizza selber machen', 'Nougat Bit Müsli', 'Porridge mit Peanutbutter', 'Cookies backen', 'Hefezopf mit Nutella', 'Obazda Brot'],
    'salty': ['salty', 'sweet', 'salty', 'salty', 'salty', 'salty', 'salty', 'salty', 'salty', 'sweet', 'sweet', 'sweet', 'sweet', 'salty'],
    'effort': [4, 1, 1, 1, 2, 2, 1, 9, 9, 2, 3, 6, 6, 4],
    'takeaway': ['takeaway', 'cook', 'takeaway', 'takeaway', 'cook', 'cook', 'cook', 'cook', 'cook', 'cook', 'cook', 'cook', 'cook', 'cook']
})

# Filter by sweet/salty
def filter_salty_sweet(food_table, salty_sweet):
    filtered_food_table = food_table[food_table['salty'] == salty_sweet]
    return filtered_food_table

# Filter by takeaway/cook at home
def filter_takeaway_cook(food_table, takeaway_cook):
    filtered_food_table = food_table[food_table['takeaway'] == takeaway_cook]
    return filtered_food_table

# Filter by effort
def filter_effort(food_table, effort):
    filtered_food_table = food_table[food_table['effort'] <= effort]
    return filtered_food_table

# Set up page
st.title("Food Inspiration")

# Ask for salty or sweet
salty_sweet = st.radio("Do you want something sweet or salty?", ('salty', 'sweet'))

# Filter by salty/sweet
filtered_food_table = filter_salty_sweet(food_table, salty_sweet)

# Ask for takeaway or cook at home
takeaway_cook = st.radio("Do you want to cook at home or get takeaway?", ('cook', 'takeaway'))

# Filter by takeaway/cook at home
filtered_food_table = filter_takeaway_cook(filtered_food_table, takeaway_cook)

# Ask for effort level
effort = st.slider("How much effort do you want to put in?", 1, 9)

# Filter by effort
filtered_food_table = filter_effort(filtered_food_table, effort)

# Suggest food
if st.button("Suggest Food"):
    # Randomly select food from filtered options
    food_options = list(filtered_food_table["food"])
    if len(food_options) == 0:
        st.write("Sorry, no food options match your preferences.")
    else:
        current_food = random.choice(food_options)
        st.write("You should try", current_food)
        st.session_state.last_food = current_food

# Suggest another food
if st.button("Try Again"):
    # Randomly select food from filtered options
    food_options = list(filtered_food_table["food"])
    if len(food_options) == 0:
        st.write("Sorry, no food options match your preferences.")
    else:
        current_food = random.choice([x for x in food_options if
