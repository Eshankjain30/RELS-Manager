import streamlit as st
from datetime import datetime
import random

def generate_gr_number():
    return f"R{random.randint(1000, 9999)}"

def main():
    st.set_page_config(page_title="Student Management")
    
    # Auto-generated fields
    gr_number = generate_gr_number()
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    st.markdown("<h2 style='text-align: center;'>APPLICATION FORM</h2>", unsafe_allow_html=True)
    
    # G.R. Number and Date
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**G.R. No.:**", gr_number)
    with col2:
        st.write("**Date:**", current_date)
    
    # Student Name
    st.text_input("First Name", key="first_name")
    st.text_input("Middle Name", key="middle_name")
    st.text_input("Last Name", key="last_name")
    
    # Date of Birth
    st.date_input("Date of Birth", format="DD-MM-YYYY", key="dob")
    
    # Gender
    st.selectbox("Gender", ["Male", "Female", "Other"], key="gender")
    
    # Aadhar Card Number
    st.text_input("Aadhar Card Number", key="aadhar")
    
    # Parents' Information
    st.text_input("Father's Name", key="father_name")
    st.text_input("Mother's Name", key="mother_name")
    st.text_input("Father's Occupation", key="father_occupation")
    st.text_input("Mother's Occupation", key="mother_occupation")
    
    # Contact Numbers
    st.text_input("Father's Contact Number", key="father_contact")
    st.text_input("Mother's Contact Number", key="mother_contact")
    st.text_input("Own Contact Number", key="own_contact")
    
    # Address
    st.text_area("Postal Address", key="address")
    st.text_input("Area", key="area")
    st.text_input("City", key="city")
    
    # Hobbies
    st.text_area("Hobbies", key="hobbies")
    
    # Admission Details
    #st.selectbox("Admission Required In", ["Standard", "Course"], key="admission")
    st.selectbox("Admission Required In", ["5th", "6th", "7th", "8th","9th", "10th"],key="admission")
    st.selectbox("Course", ["CBSE", "NCERT", "IB", "CBSE + NCERT"], key="course")

    # Previous Education
    st.text_input("School Name", key="school_name")
    st.text_input("Previous Tuition Class", key="tuition_class")
    st.text_input("Previous Result", key="previous_result")
    
    # Remarks
    st.text_area("Remark", key="remark")
    
    # Fee Confirmation
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_input("Amount", key="amount")
    with col2:
        st.selectbox("Mode", ["Single", "Double", "Monthly"], key="mode")
    with col3:
        st.text_input("With Form", key="with_form")
    
    # Buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("SAVE")
    with col2:
        st.button("UPDATE")
    with col3:
        st.button("NEW")
    
if __name__ == "__main__":
    main()