from models import db
from flask_restful import Resource
from flask import request, render_template
from models.card import Cards
from models.deck import Decks

def GetCard(id):
    c=Cards.query.filter_by(deck_id=id).all()
    return c
def GetDeck():
    d=Decks.query.order_by(Decks.name).all()
    return d


class AllCrds(Resource):
    def get(self,d_id):
        l=GetCard(d_id)
        les=[]
        for x in l:
            les.append(x.GetDict())
        return les

def AllHtmlCards(d_id):
    l=GetCard(d_id)
    k=GetDeck()
    les=[]
    dec=[]
    for x in l:
        les.append(x.GetDict())
    for y in k:
        dec.append(y.GetDict())
    #print(dec)
    #print(les)
    return render_template("cards.html",b=11,cards=les,decks=dec,i=int(d_id))
def cDummy():
    #l=GetCard(d_id)
    k=GetDeck()
    #les=[]
    dec=[]
    #for x in l:
        #les.append(x.GetDict())
    for y in k:
        dec.append(y.GetDict())
    #print(dec)
    #print(les)
    return render_template("cards.html",b=1,cards=[],decks=dec,i=0)