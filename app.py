import streamlit as st
import pandas as pd
import random
import time

# Load data from Excel file
df = pd.read_excel("food_table.xlsx")

# Define filters
herzhaft_options = ["herzhaft", "süß"]
takeaway_options = ["bestellen", "kochen"]
effort_options = ["wenig", "mittel", "hoch"]

# Define CSS styles
STYLE = """
<style>
body {
    background-image: url('https://images.unsplash.com/photo-1523520098692-64d7b0e29b8f?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTZ8fHdhbGxwYXBlcnxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80');
    background-size: cover;
}
.container {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    margin-top: 20px;
    margin-bottom: 20px;
}
h1 {
    color: #ff4500;
    text-align: center;
    animation: blink 1s linear infinite;
}
@keyframes blink {
    50% {
        opacity: 0;
    }
}
</style>
"""

# Define JS scripts
JS = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var logo = document.querySelector('#logo');
    logo.addEventListener('mouseenter', function() {
        this.style.transform = 'rotate(360deg)';
    });
    logo.addEventListener('mouseleave', function() {
        this.style.transform = 'rotate(0deg)';
    });
});
</script>
"""
st.set_page_config(page_title="Carlas Food Inspiration", page_icon=":fork_and_knife:", layout="wide")
st.markdown("<div id='logo'><img src='https://www.freeiconspng.com/uploads/restaurant-icon-png-21.png' width='50'></div>", unsafe_allow_html=True)


# Get user inputs for filters
st.write("# Carlas Food Inspiration!")
st.markdown(JS, unsafe_allow_html=True)

herzhaft = st.multiselect("herzhaft oder süß?", herzhaft_options, default=["herzhaft", "süß"])
if len(herzhaft) > 0:
    df = df[df["salty"].isin(herzhaft)]

takeaway = st.multiselect("Kochen oder Bestellen?", takeaway_options, default=["bestellen", "kochen"])
if len(takeaway) > 0:
    df = df[df["takeaway"].isin(takeaway)]
    
    if "kochen" in takeaway:
        effort = st.multiselect("Wie viel Aufwand?", effort_options, default=["wenig", "mittel", "hoch"])
        if len(effort) > 0:
            df = df[df["effort"].isin(effort)]

# Suggest food
if st.button("WAS LECKRES"):
    with st.spinner(text="Ich überlege..."):
        time.sleep(2)
    if len(df) > 0:
        current_food = random.choice(list(df["food"]))
        st.write(f"# {current_food}")
        st.write("---")
        st.button("Bäh! Ich will was leckres", key="new_suggestion")
    else:
        st.write("Leider gibt es nichts Leckeres.")

# Generate new suggestion
if "new_suggestion" in st.session_state:
    current_food = random.choice(list(df["food"]))
    st.write(f"# {current_food}")
    st.write("---")
    st.button("Bäh! Ich will was leckres", key="new_suggestion")
