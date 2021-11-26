from models import db
from flask_restful import Resource
from flask import request
from models.deck import Decks
from models.card import Cards
from models.score import Scores

def GetDeck(id):
    d=Decks.query.filter_by(id=id).first()
    return d

def GetCardsbyDeck(id):
    d=Cards.query.filter_by(deck_id=id).all()
    return d

def GetScoresbyDeck(id):
    d=Scores.query.filter_by(deck_id=id).all()
    return d


class Deck_Others(Resource):
    def get(self,deck_id):
        g=GetDeck(deck_id)
        return g.GetDict(),200

    def delete(self,deck_id):
        g=GetDeck(deck_id)
        if g==None:
            return {"Error":"Not Found"},404
        c=GetCardsbyDeck(deck_id)
        #print(c)
        if c!=None:
            for x in c:
                db.session.delete(x)
        s=GetScoresbyDeck(deck_id)
        if s!=None:
            for x in c:
                db.session.delete(c)
        db.session.delete(g)
        db.session.commit()
        return g.GetDict(),200

    def put(self,deck_id):
        g=GetDeck(deck_id)
        if request.content_type=='application/json':
            name=request.json['name']
        else:
            name=request.form['name']
        if g==None:
            return {"Error":"NotFound"},404
        if name==None:
            return {"Error":"Incorecct Parameter"},400
        g.name=name
        db.session.commit()
        g=GetDeck(deck_id)
        return g.GetDict(),200

def creteDeck(name):
    d=Decks(name=name)
    db.session.add(d)
    db.session.commit()
    return d

class Decks_Create(Resource):
    def post(self):
        if request.content_type=='application/json':
            name=request.json['name']
        else:
            name=request.form['name']
        #print(name)
        if name==None:
            return {"Error":"Incorecct Parameter"},400
        d=creteDeck(name)
        return d.GetDict(),201
