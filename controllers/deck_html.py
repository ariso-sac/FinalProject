from models import db
from flask import request, render_template, redirect
from models.deck import Decks
from models.score import Scores


def GetALLDecks():
    d = Decks.query.order_by(Decks.name).all()
    s = Scores.query.order_by(Scores.id).all()
    return render_template("index.html", decks=d,scores=s)

def GetTableDecks():
    d = Decks.query.order_by(Decks.name).all()
    return render_template("deck_modify.html", decks=d)

def CraeteTheDeck():
    name = request.form["name"]
    d = Decks(name=name)
    db.session.add(d)
    db.session.commit()
    return redirect("/")


def sendForm():
    return render_template('deck_form.html')
