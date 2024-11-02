# import streamlit as st
# import pyrebase
# import firebase_admin
# from firebase_admin import credentials, firestore
# from datetime import datetime

# # Firebase configuration for pyrebase (authentication and real-time database)
# firebaseConfig = {
#     "apiKey": "AIzaSyDMBLeFCxnMcYBAhS3l_-Vu5n5jYAeb5Ew",
#     "authDomain": "proj-58848.firebaseapp.com",
#     "projectId": "proj-58848",
#     "databaseURL": "https://proj-58848-default-rtdb.europe-west1.firebasedatabase.app/",
#     "storageBucket": "proj-58848.firebasestorage.app",
#     "messagingSenderId": "674440611624",
#     "appId": "1:674440611624:web:006d23886fb29f7098321d"
# }

# # Initialize Firebase with pyrebase for Authentication and Realtime Database
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
# db_rtdb = firebase.database()
# storage = firebase.storage()

# # Function to initialize Firebase Admin SDK and return Firestore client
# def initialize_firebase_admin():
#     if not firebase_admin._apps:
#         firebase_cred = credentials.Certificate({
#             "type": "service_account",
#             "project_id": "proj-58848",
#             "private_key_id": "9118b569aabadcfd157f9b0a8b69b03fc3626317",
#             "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC2iSuXpwAXKGLl\nfuYZa/4uTMNSXwhVr7pe4ioocjCbmpejgQUZquV8Xic1QxaaOprFpdRuYoGZaOKi\nnFhcUVUhkoQTdAgc0mE3AyBQtMH5dmiQ6OShW5IVaiQIjSk+1iz2ujO2dedXFJkK\nf8o4nh4sN+tNjNehTmKPY8BpH9boyIxjUwUXZGpedX7mwAfzMkSY1hPoH+Wc4ZdC\nKtGTN6bTpkV0LHzoWdLvZUE58e6+SRQn82WX2yOuRsCm1fI144ytrHriaA4nAG1R\nNSVULhQiSvs0IFuBELShNOYDbtPHGTwACVmmnswoJBmkTD0kITpw3V0j6jOI7ymW\nOz4v1MONAgMBAAECggEABNxu6HYX+gXnNrsw6VQ0OJgIJMog5v54vtMhRUkS0B06\nh/reuTORMsUwU4PkXU1No6rW/YbEP2LvYJFvIJJBhQhDJsasLdXqcdq0jxtC0sZo\nLxSMr8Fh1aePqxluekM3S+2WHl6FP48hKwocYNkEVUm6vsRCVjdH4UKwtC8wlXiX\nEcdegKzWm3AP2CrJjjG02ftLNDomf/a7BANam3KTasemfOAMfZV6c8rMW2eNIqgd\nBklPQyBONI5DRkwvfH52cUiJe1d8CjsglOPYQh+Juquhz2HQ3oKtNGf/mynlR1zM\nLz86tyCtNxP9Jn6HRULQSN/R6QqGvPRNN8Tnh1nanwKBgQDZORpYsBX+AhitWAQE\naUUB3Svrk4nsfrh++cEOwvX/j5Gq7rFGI/+l27gPRyFFQcTC2hTsrO5BT1g1AU8b\nNR0W7xeCNR30oIGiw6hHg6qeP+DpWJ+DpOQzAaU4CV0rV0tPd1FcFNkJv7oaAGfN\n4X2PPtrcY/uIv3rSX0BG1rX1LwKBgQDXHuRdXbUdxfn5Se/gXiJDlecXIvEDYiCe\nqhOvtzD+6dzTeS8moKAqkq3VUeRAqv4UQZJ/8/ruekNOpfj9Ar+LxNzg/cNKA/DG\nLelIP/2Xy6fEHXnajhquutQalYFRpwwjeUV0MhCxF3YB6o0QDVaYtyo2HDP9sW/q\nQDBFGEpcAwKBgGLa8tuDny6Ow643jPR499emULOP3EfNT6cxgCN4pD0emDtDD1gN\nT+2qNXR2eXSsPqAyYS1ocbE1K75LjzWhkVB7lKZECBLo7LYm9rE9AWutRGzNUSK2\n6scvq4H5+PWdb3+FnHgcYL1oDIiCwLrYMKz8/NspgTI1ee69PGJAmmQvAoGBAJgF\nwsigcmAKCq+7KoPawkgU5WyaSsxjSj4WXzcsNLnQtzfTShj4JngvlB1OdAmnTUsv\nU8KMvuZNDMfFzwGuMYMqqhVt/9aMlljXFSbz4dimGXckhXqINh8I9N+ci/kSHifr\nicOlpdoghEqyYOHZKztdJb17jNpZzIc0uWf61IHVAoGAFHWRmvE/yK4n3g85sEwZ\nWnMfb9NgIA109c79JA2YJ9cMOSBboGYb7dtgkQ0JosU+OMq+8x4OvTEYRNHOVi2C\nEg0eJlgLrksT2A8tndADOo3+n3igDptqM30cGDpewNGOHCDS4aHMVWuUa1suqXzk\nWP3an8LS7xp4yP0AI8LU5JM=\n-----END PRIVATE KEY-----\n",
#             "client_email": "firebase-adminsdk-u5ghi@proj-58848.iam.gserviceaccount.com",
#             "client_id": "117984377403170508973",
#             "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#             "token_uri": "https://oauth2.googleapis.com/token",
#             "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#             "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-u5ghi%40proj-58848.iam.gserviceaccount.com"
#         })
#         firebase_admin.initialize_app(firebase_cred)
#     return firestore.client()

# # Initialize Firestore client
# db_firestore = initialize_firebase_admin()

# # Streamlit UI
# st.sidebar.title("Community App")
# choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign up'])

# email = st.sidebar.text_input('Email address')
# password = st.sidebar.text_input('Password', type='password')

# # Sign up functionality
# if choice == 'Sign up':
#     handle = st.sidebar.text_input('Handle name', value='Default')
#     submit = st.sidebar.button('Create my account')
#     if submit:
#         user = auth.create_user_with_email_and_password(email, password)
#         st.success('Account created successfully!')
#         st.balloons()
#         auth.sign_in_with_email_and_password(email, password)
#         db_rtdb.child(user['localId']).child("Handle").set(handle)
#         db_rtdb.child(user['localId']).child("ID").set(user['localId'])
#         st.title('Welcome ' + handle)

# # Login functionality
# if choice == 'Login':
#     login = st.sidebar.checkbox('Login')
#     if login:
#         user = auth.sign_in_with_email_and_password(email, password)
#         st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
#         bio = st.radio('Navigate', ['Home', 'Workplace Feeds', 'Settings'])

#         # Settings
#         if bio == 'Settings':
#             nImage = db_rtdb.child(user['localId']).child("Image").get().val()
#             if nImage:
#                 st.image(nImage)
#             exp = st.expander('Change Bio and Image')
#             with exp:
#                 newImgPath = st.text_input('Enter full path of your profile image')
#                 if st.button('Upload'):
#                     uid = user['localId']
#                     fireb_upload = storage.child(uid).put(newImgPath, user['idToken'])
#                     img_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
#                     db_rtdb.child(user['localId']).child("Image").push(img_url)
#                     st.success('Profile updated!')

#         # Home
#         elif bio == 'Home':
#             col1, col2 = st.columns(2)
#             with col1:
#                 nImage = db_rtdb.child(user['localId']).child("Image").get().val()
#                 if nImage:
#                     st.image(nImage, use_column_width=True)
#                 post = st.text_input("Share your current mood", max_chars=100)
#                 if st.button('Share Post'):
#                     now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#                     post_data = {'Post': post, 'Timestamp': now}
#                     db_rtdb.child(user['localId']).child("Posts").push(post_data)
#                     st.balloons()

#             with col2:
#                 all_posts = db_rtdb.child(user['localId']).child("Posts").get()
#                 if all_posts.val():
#                     for Posts in reversed(all_posts.each()):
#                         st.code(Posts.val(), language='')

#         # Workplace Feeds
#         else:
#             all_users = db_rtdb.get()
#             res = [u.val()["Handle"] for u in all_users.each()]
#             choice = st.selectbox('Colleagues', res)
#             if st.button('Show Profile'):
#                 for users_handle in all_users.each():
#                     if users_handle.val()["Handle"] == choice:
#                         lid = users_handle.val()["ID"]
#                         handlename = db_rtdb.child(lid).child("Handle").get().val()
#                         st.markdown(handlename)
#                         nImage = db_rtdb.child(lid).child("Image").get().val()
#                         if nImage:
#                             st.image(nImage)
#                         all_posts = db_rtdb.child(lid).child("Posts").get()
#                         if all_posts.val():
#                             for Posts in reversed(all_posts.each()):
#                                 st.code(Posts.val(), language='')

# # Admin Dashboard for Client Management
# def admin_dashboard():
#     st.title("Admin Dashboard")
#     email = st.text_input("Client email for access approval:")
#     expiry_date = st.date_input("Expiry date for client", value=datetime(2024, 12, 31))
#     dashboards = st.multiselect("Dashboards to access", ['dashboard1', 'dashboard2', 'dashboard3'])

#     if st.button("Add Client"):
#         username = email.split('@')[0]
#         client_data = {
#             'username': username,
#             'email': email,
#             'permissions': dashboards,
#             'expiry_date': expiry_date.strftime('%Y-%m-%d'),
#             'login_status': 0
#         }
#         db_firestore.collection('clients').document(username).set(client_data)
#         st.success(f"Client '{email}' added successfully!")

# if __name__ == "__main__":
#     admin_dashboard()




# Complete code for admin_autocred.py

import streamlit as st
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyDMBLeFCxnMcYBAhS3l_-Vu5n5jYAeb5Ew",
    "authDomain": "proj-58848.firebaseapp.com",
    "projectId": "proj-58848",
    "databaseURL": "https://proj-58848-default-rtdb.europe-west1.firebasedatabase.app/",
    "storageBucket": "proj-58848.firebasestorage.app",
    "messagingSenderId": "674440611624",
    "appId": "1:674440611624:web:006d23886fb29f7098321d"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db_rtdb = firebase.database()
storage = firebase.storage()

# Function to initialize Firebase Admin SDK and return Firestore client
def initialize_firebase_admin():
    if not firebase_admin._apps:
        firebase_cred = credentials.Certificate({
            "type": st.secrets["firebase_credentials"]["type"],
            "project_id": st.secrets["firebase_credentials"]["project_id"],
            "private_key_id": st.secrets["firebase_credentials"]["private_key_id"],
            "private_key": st.secrets["firebase_credentials"]["private_key"].replace("\\n", "\n"),
            "client_email": st.secrets["firebase_credentials"]["client_email"],
            "client_id": st.secrets["firebase_credentials"]["client_id"],
            "auth_uri": st.secrets["firebase_credentials"]["auth_uri"],
            "token_uri": st.secrets["firebase_credentials"]["token_uri"],
            "auth_provider_x509_cert_url": st.secrets["firebase_credentials"]["auth_provider_x509_cert_url"],
            "client_x509_cert_url": st.secrets["firebase_credentials"]["client_x509_cert_url"]
        })
        firebase_admin.initialize_app(firebase_cred)
    return firestore.client()

db_firestore = initialize_firebase_admin()

# Streamlit UI for Admin
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

