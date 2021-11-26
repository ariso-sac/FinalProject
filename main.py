from os import environ
from controllers.scores import Scores_Api
from controllers.cards import Cards_Create, Cards_Others
from controllers.decks import Decks_Create, Deck_Others
from controllers.deck_html import GetALLDecks, CraeteTheDeck, sendForm, GetTableDecks
from controllers.cardsbydeck import AllCrds, AllHtmlCards, cDummy
from models.score import Scores
from models.card import Cards
from models.deck import Decks
from models.users import user_datastore
from models import db
from flask import Flask, render_template, request, redirect
from flask_security import login_required, Security, logout_user
from flask_restful import Resource, Api
import os

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = 'HelloWorld'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

# Create database connection object
db.init_app(app)
security = Security(app, user_datastore)

# Create a user to test with


@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='sachin@mail.com', password='root')
    db.session.commit()


# '''
# Views
@app.route('/')
@login_required
def index():
    return GetALLDecks()


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/create/deck', methods=['GET', 'POST'])
def crtdck():
    if request.method == "GET":
        return sendForm()
    if request.method == "POST":
        return CraeteTheDeck()


@app.route('/modify/deck')
def dckmod():
    return GetTableDecks()


@app.route('/cards', methods=['GET', 'POST'])
def crds():
    if request.method == 'POST':
        d_id = request.form['name']
        return AllHtmlCards(d_id)
    if request.method == 'GET':
        return cDummy()


@app.route("/final/<d>/<n>")
def final(d, n):
    return render_template('quiz.html', id=d, name=n)


# Api Intialisation
api = Api(app)
api.add_resource(Decks_Create, '/api/deck')
api.add_resource(Deck_Others, '/api/deck/<deck_id>')
api.add_resource(Cards_Create, '/api/card')
api.add_resource(Cards_Others, '/api/card/<card_id>')
api.add_resource(Scores_Api, '/api/user/<u_id>/deck/<d_id>')
api.add_resource(AllCrds, '/api/cardsbydeck/<d_id>')

if __name__ == '__main__':
    app.run(port=environ.get("PORT", 8080), host='0.0.0.0', debug=True)
