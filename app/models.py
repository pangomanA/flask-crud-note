from app import db
from datetime import datetime, timezone

class Note(db.Model):

    uid: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title: str = db.Column(db.String(100), unique=True, nullable=False)
    body: str = db.Column(db.Text, nullable=True)
    created: datetime = db.Column(db.DateTime, default=datetime.now(timezone.utc))

