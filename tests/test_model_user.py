import pytest
from app.auth.models import User
import datetime

def test_create_user(db):
    user1 = User(name="user1", email="email_1@gmail.com")
    user1.set_password("password1")
    user1.save()
    user2 = User(name="user2", email="email_2@gmail.com")
    user2.set_password("password2")
    user2.save()
    count = db.session.query(User).count()
    assert count is 2

"""
def test_meeting_creation(db):
    meeting = app.models.Meeting(
        _date = datetime.datetime.strptime('2018-12-19', "%Y-%m-%d"),
    )
    db.session.add(meeting)
    db.session.commit()
"""