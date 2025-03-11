import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# Initialize database connection
def get_db_connection():
    conn = sqlite3.connect("expenses.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        type TEXT,
                        category TEXT,
                        amount REAL,
                        date TEXT)''')
    return conn

# Function to add a transaction to the database
def add_transaction(type, category, amount, date):
    conn = get_db_connection()
    conn.execute("INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)", 
                 (type, category, amount, date))
    conn.commit()
    conn.close()

# Function to fetch all transactions from the database
def fetch_transactions():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM transactions", conn)
    conn.close()
    return df

# Streamlit UI
def main():
    st.set_page_config(page_title="Expense Manager")
    
    st.markdown("""
        <style>
            body {background-color: #000000; color: #FFFFFF;}
            .stApp {background-color: #000000;}
            .css-18e3th9 {background-color: #000000;}
            .css-1d391kg {color: #FFA500;}
            .stButton>button {background-color: #FFA500; color: #FFFFFF;}
            .dataframe {background-color: transparent !important;}
            section[data-testid='stSidebar'] {display: none !important;}
            div[data-testid='collapsedControl'] {display: none !important;}
            #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    st.title("💰 Expense & Income Manager")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Add Transaction")
        type = st.selectbox("Type", ["Income", "Expense"])
        if type == "Income":
            category = st.selectbox("Category", ["Fees", "Others"])
        else:
            category = st.selectbox("Category", ["LightBill", "Rent", "Brokerage", "Personal", "Others"])
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        date = st.date_input("Date", value=datetime.today()).strftime('%d-%b-%y')
        
        if st.button("Add Transaction"):
            add_transaction(type, category, amount, date)
            st.success("Transaction added successfully!")
    
    with col2:
        st.header("Current Income")
        df = fetch_transactions()
        income = df[df["type"] == "Income"]["amount"].sum()
        expenses = df[df["type"] == "Expense"]["amount"].sum()
        balance = income - expenses
        
        st.metric(label="Total Income", value=f"₹{income:.2f}")
        st.metric(label="Total Expenses", value=f"₹{expenses:.2f}", delta=f"-₹{expenses:.2f}")
        st.metric(label="Current Balance", value=f"₹{balance:.2f}", delta=f"{balance:.2f}")
    
    st.header("📜 Balance Sheet")
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"]).dt.strftime('%d-%b-%y')
        df["amount"] = df["amount"].apply(lambda x: f"{x:.2f}")
        st.dataframe(df.style.set_properties(**{'background-color': 'transparent', 'color': 'white'}))
    else:
        st.info("No transactions recorded yet.")

if __name__ == "__main__":
    main()
