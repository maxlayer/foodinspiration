import streamlit as st
import pandas as pd
import random
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from streamlit_webrtc import ClientSettings
import streamlit.components.v1 as components

st.set_page_config(page_title="Food Inspiration für Carla", page_icon=":fork_and_knife:", layout="wide")

# Load data from Excel file
df = pd.read_excel("food_table.xlsx")

# Define filters
herzhaft_options = ["All", "herzhaft", "süß"]
takeaway_options = ["All", "bestellen", "kochen"]
effort_options = ["All", "wenig", "mittel", "hoch", "bestellen"]

# Define variables for swipe cards
swipe_cards = []
swipe_index = 0

# Define a class to capture video from the user's camera
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        return frame

# Create a function to display a swipe card for a food suggestion
def create_swipe_card(food):
    return f"""
        <div class="swipe-card">
            <h2>{food}</h2>
        </div>
    """

# Create a function to generate swipe cards for all food suggestions in the dataframe
def generate_swipe_cards():
    global swipe_cards
    global swipe_index
    swipe_cards = [create_swipe_card(food) for food in df["food"]]
    swipe_index = 0

# Generate swipe cards when the app starts
generate_swipe_cards()

# Define the HTML and CSS for the swipe cards and swipe container
swipe_css = """
    <style>
    .swipe-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 50px;
    }

    .swipe-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
        width: 80%;
        height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
        position: absolute;
        z-index: 1;
        transform: translateX(-50%) translateY(-50%) rotate(0deg);
        transition: transform 0.5s ease;
    }

    .swipe-card h2 {
        font-size: 48px;
        text-align: center;
    }

    .swipe-card.yes {
        transform: translateX(-50%) translateY(-50%) rotate(30deg) translateX(500px);
    }

    .swipe-card.no {
        transform: translateX(-50%) translateY(-50%) rotate(-30deg) translateX(-500px);
    }
    </style>
"""

swipe_html = f"""
    <div class="swipe-container">
        <div id="swipe-card-container">
            {"".join(swipe_cards)}
        </div>
    </div>
"""

# Define the JavaScript for the swipe events
swipe_js = """
    <script src="https://hammerjs.github.io/dist/hammer.js"></script>
    <script>
    var swipeContainer = document.getElementById('swipe-card-container');
    var cards = swipeContainer.getElementsByClassName('swipe-card
