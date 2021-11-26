from models import db
from models.deck import Decks
from models.users import User


class Scores(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    easy = db.Column(db.Integer(), default=0)
    moderate = db.Column(db.Integer(), default=0)
    hard = db.Column(db.Integer(), default=0)
    deck_id = db.Column(db.Integer, db.ForeignKey(
        Decks.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        User.id), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def GetDict(self):
        return {
            "id": self.id,
            "easy": self.easy,
            "moderate": self.moderate,
            "hard": self.hard,
            "user_id": self.user_id,
            "deck_id": self.deck_id
        }
