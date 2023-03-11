import streamlit as st
import pandas as pd
from github import Github

def customize_table():
    # Authenticate to Github using your PAT
    g = Github("YOUR_PERSONAL_ACCESS_TOKEN")

    # Specify the Github repository and Excel file
    repo = g.get_repo("YOUR_REPOSITORY")
    file_path = "path/to/food_table.xlsx"

    # Load data from Excel file
    df = pd.read_excel(f"https://github.com/{repo.full_name}/raw/main/{file_path}")

    # Display the current data
    st.write("Current data:")
    st.write(df)

    # Allow the user to modify the data
    st.write("Modify data:")
    new_df = df.copy()
    new_df.loc[0, "food"] = st.text_input("Enter a new food:", df.loc[0, "food"])
    new_df.loc[0, "salty"] = st.selectbox("Is it salty or sweet?", ["salty", "sweet"], index=int(df.loc[0, "salty"]=="sweet"))
    new_df.loc[0, "effort"] = st.selectbox("Effort level:", ["wenig", "mittel", "hoch"], index=["wenig", "mittel", "hoch"].index(df.loc[0, "effort"]))
    new_df.loc[0, "takeaway"] = st.selectbox("Takeaway or cook it yourself?", ["bestellen", "kochen"], index=int(df.loc[0, "takeaway"]=="kochen"))

    # Save the modified data to Github
    if st.button("Save changes"):
        contents = repo.get_contents(file_path)
        repo.update_file(contents.path, "Update food table", new_df.to_excel(None, index=False), contents.sha)
        st.write("Changes saved!")
