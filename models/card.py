from models import db
from models.deck import Decks


class Cards(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    front = db.Column(db.String(25), unique=True)
    back = db.Column(db.String(20), unique=True)
    deck_id = db.Column(db.Integer, db.ForeignKey(
        Decks.id), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
    db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def GetDict(self):
        return {"id": self.id, "front": self.front, "back": self.back, "deck_id": self.deck_id}
