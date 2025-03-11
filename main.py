import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="RELS Classes")
    
    # Custom CSS for styling
    st.markdown("""
        <style>
            body {background-color: #000000; color: #FFFFFF;}
            .stApp {background-color: #000000;}
            .css-18e3th9 {background-color: #000000;}
            .css-1d391kg {color: #FFA500;}
            .stButton>button {background-color: #FFA500; color: #FFFFFF; width: 100%; padding: 10px; font-size: 18px;}
            .header {text-align: center; font-size: 32px; font-weight: bold; color: #FFA500;}
            .st-emotion-cache-1gulkj5 {display: none;}
            section[data-testid='stSidebar'] {display: none !important;}
            div[data-testid='collapsedControl'] {display: none !important;}
            #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    # Load and display image
    image = Image.open("rels_classes_logo.png")  # Ensure the image file is available in the directory
    st.image(image, use_container_width=True)
    
    st.markdown("<div class='header'>Welcome to RELS Classes</div>", unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Student Management"):
            st.switch_page("pages/student_management.py")  # Placeholder for student management module
    
    with col2:
        if st.button("Accounts"):
            st.switch_page("pages/accounts.py")  # Placeholder for accounts module
    
if __name__ == "__main__":
    main()
