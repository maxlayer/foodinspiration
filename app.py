import streamlit as st
import pandas as pd
import random
from streamlit_aggrid import GridOptionsBuilder, AgGrid, DataReturnMode, JsCode

st.set_page_config(page_title="Food Inspiration für Carla", page_icon=":fork_and_knife:", layout="wide")

# Load data from Excel file
df = pd.read_excel("food_table.xlsx")

# Define filters
herzhaft_options = ["All", "herzhaft", "süß"]
takeaway_options = ["All", "bestellen", "kochen"]
effort_options = ["All", "wenig", "mittel", "hoch", "bestellen"]

# Get user inputs for filters
st.write("# Welcome to Food Inspiration!")
st.write("Use the following filters to find your perfect food:")

herzhaft = st.selectbox("herzhaft oder süß?", herzhaft_options)
if herzhaft != "All":
    df = df[df["salty"] == herzhaft]

takeaway = st.selectbox("Kochen oder Bestellen?", takeaway_options)
if takeaway != "All":
    df = df[df["takeaway"] == takeaway]
    
    if takeaway == "kochen":
        effort = st.selectbox("How much effort?", effort_options)
        if effort != "All":
            df = df[df["effort"] == effort]

# Suggest food
if st.button("WAS LECKRES"):
    if len(df) > 0:
        food_list = list(df["food"])
        grid_options = GridOptionsBuilder.from_dataframe(df) \
            .enable_selection() \
            .enable_pagination() \
            .enable_filtering() \
            .enable_sorting() \
            .pagination_autoPageSize(True) \
            .build()

        food_returned = AgGrid(
            df,
            gridOptions=grid_options,
            data_return_mode=DataReturnMode.AS_ROWS,
            update_mode=AgGrid.UpdateMode.SELECTION_CHANGED,
            height=400,
            width='100%',
            theme='streamlit',
            key="food_grid"
        )

        if food_returned['event'] == 'SelectionChanged':
            selected_rows = food_returned['data']
            liked_foods = []
            disliked_foods = []
            for row in selected_rows:
                if row['liked'] == True:
                    liked_foods.append(row['food'])
                elif row['liked'] == False:
                    disliked_foods.append(row['food'])
            st.write("Liked Foods:")
            st.write(liked_foods)
            st.write("Disliked Foods:")
            st.write(disliked_foods)
    else:
        st.write("Leider gibt es nichts Leckeres.")

st.write("Food data source: [www.example.com/food](http://www.example.com/food)")
