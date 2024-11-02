
import streamlit as st
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Firebase configuration for pyrebase (authentication and real-time database)
firebaseConfig = {
    "apiKey": "AIzaSyDMBLeFCxnMcYBAhS3l_-Vu5n5jYAeb5Ew",
    "authDomain": "proj-58848.firebaseapp.com",
    "projectId": "proj-58848",
    "databaseURL": "https://proj-58848-default-rtdb.europe-west1.firebasedatabase.app/",
    "storageBucket": "proj-58848.firebasestorage.app",
    "messagingSenderId": "674440611624",
    "appId": "1:674440611624:web:006d23886fb29f7098321d"
}

# Initialize Firebase with pyrebase for Authentication and Realtime Database
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db_rtdb = firebase.database()
storage = firebase.storage()

# Function to initialize Firebase Admin SDK and return Firestore client
def initialize_firebase_admin():
    if not firebase_admin._apps:
        firebase_cred = credentials.Certificate({
            "type": "service_account",
            "project_id": "proj-58848",
            "private_key_id": "3e86ad8f5bfc01c1eafeb8e0ef60b143acc29c3c",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCiXreMMU5T74Xh\nsZy5u4Jb7N6m4dI5A6xqLpun+/cBdbKkkFlwNlIIfEksko7wfa0nWEkCQXgjabx0\nJP5Io9NUJw+2SsssjC1idwxzTjfwO4dR0iV4aJRMnz7RXdQLqjYT2QIKlJJP7LF6\nxJXhOEayaoseS9OHSqy3tamBDTx5QMiEUvoCRUvBxk8LsMtpwRMWn66l1n/BvR5E\nOjSvPKi4KVgoYFhWA5l2w4f7nZjwFYMKQYE1vBEtxZ48ucA53hf8YaX8n6Fd0OVM\nTEr1bUAa0g0SekB8hGaNHfUmgLg7o/7na2Y3rdRX6Y+SERSmXe24vfuUpgPLPjR6\nYPM8w73VAgMBAAECggEAJb4iqGHltTkeQ+JHbh0aJkgfUWd4uGwULfJ7mEbHmf1D\n82DiiWT3GKXbVJMUyu5Ly7OH9RBG3uR7O/xFZ5k9THhv/I3SQJ6tBhBqQntSIXOU\n9v4EW8LjhhQWRBCtc7CzNVXiVZdHk3CPqNv9gwbT2DFP+VDi8LX5BBMkPa1X+08n\nBAYSIfcqpcn6/CoI9hO/NZREU7YeS22uUPxCJ74JYwJWlMhaA09WUMBtRyfMdV+D\n8R77DjvFaY7is8pFLrODX2GnX8Y27AX20QiN3lYP60cwVCwwMi3N+LEtlU4DLC9c\ny71eQb0S0+7GzJsjmcsgbOpwKJJA7TmDZMQlepyUQQKBgQDM9Wdm2SSkr9BBUxIj\nOxTJaDxb2asyDDLzih4oGbV5zijPyZO5SgumMQeni/OiUiyfUVtBa5uwLFoTYndD\nDM40sOLhLnx9XBt0+24EGjWML7+Be1OaBJDyuNlaA8Pc1phBGGilXYtD6uHqrN9V\ntYAmi3U6AK8lLUkpbDKTfCMvvQKBgQDKzjARQtmo+EX2frG6XOg5hs4rCdWRGlVn\nrr10RJgjCFJx3fXQBVMr5vGmkYYTTJwjVV4YlL3PQSNHUhfbOzu/FTujirl2T6q0\nDhBoA3LiT08/8n3cCQHvd+y2uHkGpW6JF1Wqt//ewGum/UsEMYSTc648xZB4p+6D\nPJHAd2z7+QKBgAIqBTF80Xo7sQM/kU117j5CL4D4x2n73v3bU34w502l86BeDIVE\nVuMmWWJXg/cOzxHPlhsWu8ocbccOnxvCIttDkuG1z/Ky6kdN8Fdyv2X/ixIe7z8N\nFUq60PC2YXcPfQQS8eftGO9ap5AGy0ToabX+evplz3OhCsi5L7+G7AgxAoGBALm9\nOTy10w7zw2/L/Q5HxM/a7LtyGEz6pzl8SjtQD14WYxuyQ00vc0sEClGZegf25BFg\nP/uXTnegmqTZRMweZcvNsH9JsC3xLNAXCWOZtQAbzuMsPaTmAwXE+eEm9oDlxmR8\nIJNoTUk/Rdj8plXC3D8HdY5nCrfWZZWARaTWO9RRAoGAKBpW8hVCfMCRq4543UDd\nVFooXUkxG4wAgov/z2NswxLe/sFFgmdu3kv9UKCEYFeNXl4ZtnmVp0ocoy/qsE+c\n3/lpigyNyQsl5bstch7MwmwuFC9A6lt+JUslefYF7fQlCwKlG3pjeO9Q2tk8FBtS\nA32H7jUnFefivMoTxpLN02k=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-u5ghi@proj-58848.iam.gserviceaccount.com",
            "client_id": "117984377403170508973",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-u5ghi%40proj-58848.iam.gserviceaccount.com"
        })
        firebase_admin.initialize_app(firebase_cred)
    return firestore.client()

# Initialize Firestore client
db_firestore = initialize_firebase_admin()

# Streamlit UI
st.sidebar.title("Community App")
choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign up'])

email = st.sidebar.text_input('Email address')
password = st.sidebar.text_input('Password', type='password')

# Sign up functionality
if choice == 'Sign up':
    handle = st.sidebar.text_input('Handle name', value='Default')
    submit = st.sidebar.button('Create my account')
    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Account created successfully!')
        st.balloons()
        auth.sign_in_with_email_and_password(email, password)
        db_rtdb.child(user['localId']).child("Handle").set(handle)
        db_rtdb.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome ' + handle)

# Login functionality
if choice == 'Login':
    login = st.sidebar.checkbox('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email, password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        bio = st.radio('Navigate', ['Home', 'Workplace Feeds', 'Settings'])

        # Settings
        if bio == 'Settings':
            nImage = db_rtdb.child(user['localId']).child("Image").get().val()
            if nImage:
                st.image(nImage)
            exp = st.expander('Change Bio and Image')
            with exp:
                newImgPath = st.text_input('Enter full path of your profile image')
                if st.button('Upload'):
                    uid = user['localId']
                    fireb_upload = storage.child(uid).put(newImgPath, user['idToken'])
                    img_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                    db_rtdb.child(user['localId']).child("Image").push(img_url)
                    st.success('Profile updated!')

        # Home
        elif bio == 'Home':
            col1, col2 = st.columns(2)
            with col1:
                nImage = db_rtdb.child(user['localId']).child("Image").get().val()
                if nImage:
                    st.image(nImage, use_column_width=True)
                post = st.text_input("Share your current mood", max_chars=100)
                if st.button('Share Post'):
                    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    post_data = {'Post': post, 'Timestamp': now}
                    db_rtdb.child(user['localId']).child("Posts").push(post_data)
                    st.balloons()

            with col2:
                all_posts = db_rtdb.child(user['localId']).child("Posts").get()
                if all_posts.val():
                    for Posts in reversed(all_posts.each()):
                        st.code(Posts.val(), language='')

        # Workplace Feeds
        else:
            all_users = db_rtdb.get()
            res = [u.val()["Handle"] for u in all_users.each()]
            choice = st.selectbox('Colleagues', res)
            if st.button('Show Profile'):
                for users_handle in all_users.each():
                    if users_handle.val()["Handle"] == choice:
                        lid = users_handle.val()["ID"]
                        handlename = db_rtdb.child(lid).child("Handle").get().val()
                        st.markdown(handlename)
                        nImage = db_rtdb.child(lid).child("Image").get().val()
                        if nImage:
                            st.image(nImage)
                        all_posts = db_rtdb.child(lid).child("Posts").get()
                        if all_posts.val():
                            for Posts in reversed(all_posts.each()):
                                st.code(Posts.val(), language='')

# Admin Dashboard for Client Management
def admin_dashboard():
    st.title("Admin Dashboard")
    email = st.text_input("Client email for access approval:")
    expiry_date = st.date_input("Expiry date for client", value=datetime(2024, 12, 31))
    dashboards = st.multiselect("Dashboards to access", ['dashboard1', 'dashboard2', 'dashboard3'])

    if st.button("Add Client"):
        username = email.split('@')[0]
        client_data = {
            'username': username,
            'email': email,
            'permissions': dashboards,
            'expiry_date': expiry_date.strftime('%Y-%m-%d'),
            'login_status': 0
        }
        db_firestore.collection('clients').document(username).set(client_data)
        st.success(f"Client '{email}' added successfully!")

if __name__ == "__main__":
    admin_dashboard()
