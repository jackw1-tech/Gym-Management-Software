import os
import firebase_admin
from firebase_admin import credentials, firestore

cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not os.path.exists(cred_path):
    print(f"File not found: {cred_path}")
else:
    print("File found.")
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)
db = firestore.client()
print("Connected to Firestore successfully.")