import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import os
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app


project_id = os.getenv("PROYECT_ID")
cred = credentials.ApplicationDefault()
initialize_app(
    cred,
    {
        "projectId": project_id,
    },
)


db = firestore.client()


def get_users():
    return db.collection("users").get()


def get_user_by_id(user_id):
    return db.collection("users").document(user_id).get()


def get_todos(user_id):
    return db.collection("users").document(user_id).collection("todos").get()


users = get_users()
todos_snapshot = get_todos(user_id="bernardo@gmail.com")


for u in users:
    print(u.id)
    user = u.to_dict()
    print(user)

for todos in todos_snapshot:
    todo = todos.to_dict()["description"]
    print(todo)

def get_by_id(user_id):
    user_doc = db.collection("users").document(user_id).get()
    name = user_doc.to_dict()['name']
    email = user_doc.id
    password = user_doc.to_dict()['password']
    return User(name=name, email=email, password=password, is_admin=False)
