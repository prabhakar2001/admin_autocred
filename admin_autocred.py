# admin(autocred).py
import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
firebase_cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "proj-58848",
    "private_key_id": "68012f3a1525113d3d5ca7577d93d481fbca624b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE 
KEY-----\n",
    "client_email": "firebase-adminsdk-u5ghi@proj-58848.iam.gserviceaccount.com",
    "client_id": "117984377403170508973",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": 
"https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-u5ghi%40proj-58848.iam.gserviceaccount.com"
})
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
        st.write(f"**Username:** {client_data['username']} | **Email:** {client_data['email']} 
| **Expiry Date:** {client_data['expiry_date']} | **Dashboards Access:** {', 
'.join(client_data['permissions'])} | **Status:** {login_status}")
        
        # Add a button to reset the login status for each client
        if login_status == "Logged In":
            if st.button(f"Reset Login Status for {client_data['username']}"):
                update_login_status(client_data['username'], 0)
                st.success(f"Login status for {client_data['username']} has been reset.")

# Run the admin dashboard
if __name__ == "__main__":
    admin_dashboard()

