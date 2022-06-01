from flask_login import UserMixin

from werkzeug.security import check_password_hash, generate_password_hash

from app.firestore_service import db


class User(UserMixin):
    def __init__(self, name, email, password, is_admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def get_id(self):
        return (self.email)

    def __repr__(self):
        return f"<User {self.email}>"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        user_data = db.collection("users").document(self.email)
        user_data.set({
            'name': self.name,
            'password': self.password,
            'is_admin': self.is_admin
        })

    def delete(self):
        pass

    @staticmethod
    def get_by_id(user_id):
        user_doc = db.collection("users").document(user_id).get()
        name = user_doc.to_dict()['name']
        email = user_doc.id
        password = user_doc.to_dict()['password']
        return User(name=name, email=email, password=password, is_admin=False)

    @staticmethod
    def get_all():
        return db.collection("users").get()
