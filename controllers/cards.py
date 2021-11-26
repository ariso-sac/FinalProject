from models import db
from flask_restful import Resource
from flask import request
from models.card import Cards

def GetCard(id):
    c=Cards.query.filter_by(id=id).first()
    return c

class Cards_Others(Resource):
    def get(self,card_id):
        g=GetCard(card_id)
        return g.GetDict(),200

    def delete(self,card_id):
        g=GetCard(card_id)
        if g==None:
            return {"Error":"Not Found"},404
        db.session.delete(g)
        db.session.commit()
        return g.GetDict(),200

    def put(self,card_id):
        g=GetCard(card_id)
        if g==None:
            return {"Error":"Not Found"},404
        front=request.form['front']
        back=request.form['back']
        deck=request.form['deck']
        if request.content_type=='application/json':
            front=request.json['front']
            back=request.json['back']
            deck=request.json['deck']
        else:
            front=request.form['front']
            back=request.form['back']
            deck=request.form['deck']
        if front==None or back==None or deck==None:
            return {"Error":"Wrong Input"},400 
        g.front=front
        g.back=back
        g.deck_id=deck
        db.session.commit()
        g=GetCard(card_id)
        return g.GetDict()

def createCard(Front,Back,Deck):
    d=Cards(front=Front,back=Back,deck_id=Deck)
    db.session.add(d)
    db.session.commit()
    return d

class Cards_Create(Resource):
    def post(self):
        if request.content_type=='application/json':
            front=request.json['front']
            back=request.json['back']
            deck=request.json['deck']
        else:
            front=request.form['front']
            back=request.form['back']
            deck=request.form['deck']
        #print(name)
        if front==None or back==None or deck==None:
            return {"Error":"Wrong Input"},400
        d=createCard(front,back,deck)
        return d.GetDict(),201
