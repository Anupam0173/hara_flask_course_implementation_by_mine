from app.catalog import catalog
from app import db
from flask import render_template
from app.catalog.models import Book,Publication
from app import login_manager

# @login_manager.user_loader
@catalog.route('/')
def display_books():
    books = Book.query.all()
    return render_template("home.html",books=books)

@catalog.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher_id).all()
    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)