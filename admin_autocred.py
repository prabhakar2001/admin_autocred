# admin(autocred).py
import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials from the JSON file
firebase_cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(firebase_cred)
db = firestore.client()

# Function to add a client with email, expiry date, and permissions
def add_client(email, expiry_date, permissions):
    username = email.split('@')[0]
    client_data = {
        'username': username,
        'password': '',
        'expiry_date': expiry_date.strftime('%Y-%m-%d'),
        'permissions': permissions,
        'email': email,
        'login_status': 0
    }
    db.collection('clients').document(username).set(client_data)

# Function to update login status
def update_login_status(username, status):
    db.collection('clients').document(username).update({'login_status': status})

# Admin Dashboard Interface
def admin_dashboard():
    st.title("Admin Dashboard")
    st.write("Add approved emails with permissions and expiry dates for client access.")

    # Section to add a new client's email, permissions, and expiry date
    email = st.text_input("Enter client's email for account creation approval:")
    expiry_date = st.date_input("Set expiry date for the client", value=datetime(2024, 12, 31))
    dashboards = st.multiselect("Dashboards to provide access to:", ['dashboard1', 
'dashboard2', 'dashboard3', 'dashboard4', 'dashboard5', 'dashboard6'])

    if st.button("Add Client"):
        if email and dashboards:
            add_client(email, expiry_date, dashboards)
            st.success(f"Client with email '{email}' added successfully!")
        else:
            st.error("Please provide an email and select at least one dashboard.")

    st.write("---")

    # Display all clients with their email, permissions, and expiry dates
    clients = db.collection('clients').stream()
    st.write("### Approved Clients:")
    for client in clients:
        client_data = client.to_dict()
        login_status = "Logged In" if client_data['login_status'] == 1 else "Logged Out"
        st.write(f"**Username:** {client_data['username']} | **Email:** {client_data['email']} | "
         f"**Expiry Date:** {client_data['expiry_date']} | **Dashboards Access:** {', '.join(client_data['permissions'])} | "
         f"**Status:** {login_status}")
        
        # Add a button to reset the login status for each client
        if login_status == "Logged In":
            if st.button(f"Reset Login Status for {client_data['username']}"):
                update_login_status(client_data['username'], 0)
                st.success(f"Login status for {client_data['username']} has been reset.")

# Run the admin dashboard
if __name__ == "__main__":
    admin_dashboard()

