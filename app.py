import streamlit as st
import pandas as pd
import random
import time

# Load data from Excel file  
try:  
    df = pd.read_excel("food_table.xlsx")  
except Exception as e:  
    st.error(f"Fehler beim Laden der Excel-Datei: {e}")  
    df = pd.DataFrame(columns=["food", "salty", "takeaway", "effort", "cost"])  
  
# Define filters and options  
herzhaft_options = ["herzhaft", "süß"]  
takeaway_options = ["bestellen", "kochen"]  
effort_options = ["wenig", "mittel", "hoch"]  
cost_options = ["€", "€€", "€€€"]  

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

# Page configuration
st.set_page_config(page_title="Carlas Food Inspiration", page_icon=":fork_and_knife:", layout="wide")
st.markdown("<div id='logo'><img src='https://www.freeiconspng.com/uploads/restaurant-icon-png-21.png' width='50'></div>", unsafe_allow_html=True)

# Seitenleiste für das Durchsuchen der Menüs und Hinzufügen neuer Mahlzeiten  
with st.sidebar:  
    st.write("## Alle leckeren Sachen")  
    # Suchfeld  
    search_query = st.text_input("Suche nach Mahlzeiten")  
    if search_query:  
        search_results = df[df['food'].str.contains(search_query, case=False, na=False)]  
        st.write("Suchergebnisse:")  
        for _, row in search_results.iterrows():  
            st.write(f"- {row['food']}")  
  
    # Button zum Hinzufügen einer neuen Mahlzeit  
    if st.button("Neue Mahlzeit hinzufügen"):  
        # Sie können auch st.session_state verwenden, um den Zustand des Formulars zu verwalten  
        st.session_state.show_form = True  
  
# Prüfen, ob das Formular angezeigt werden soll  
if st.session_state.get('show_form', False):  
    with st.form("new_meal_form", clear_on_submit=True):  
        st.write("### Füge eine neue Mahlzeit hinzu")  
        new_food = st.text_input("Name der Mahlzeit")  
        new_salty = st.selectbox("Herzhaft oder süß?", herzhaft_options)  
        new_takeaway = st.selectbox("Kochen oder Bestellen?", takeaway_options)  
        new_effort = st.selectbox("Wie viel Aufwand?", effort_options)  
        new_cost = st.selectbox("Kosten?", cost_options)  
  
        submit_button = st.form_submit_button("Mahlzeit speichern")  
        if submit_button:  
            # Daten zur DataFrame hinzufügen  
            new_data = {  
                "food": new_food,  
                "salty": new_salty,  
                "takeaway": new_takeaway,  
                "effort": new_effort,  
                "cost": new_cost  
            }  
            df = df.append(new_data, ignore_index=True)  
            # Die aktualisierte DataFrame in einer Excel-Datei speichern  
            try:  
                df.to_excel("food_table.xlsx", index=False)  
                st.success("Mahlzeit erfolgreich hinzugefügt!")  
                # Formular ausblenden nach dem Hinzufügen  
                st.session_state.show_form = False  
            except Exception as e:  
                st.error(f"Fehler beim Speichern der neuen Mahlzeit: {e}")  
                
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
