from flask_login import login_required
from app.catalog import catalog
from app import db
from flask import render_template,request,flash,redirect,url_for
from app.catalog.models import Book,Publication
from app import login_manager
from app.catalog.forms import EditBookForm

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


@catalog.route('/book/delete/<book_id>', methods=['GET', 'POST'])
# @login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully')
        return redirect(url_for('catalog.display_books'))
    return render_template('delete_book.html', book=book, book_id=book.id)

@catalog.route('/edit/book/<book_id>', methods=['GET', 'POST'])
# @login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash('Book Edited Successfully')
        return redirect(url_for('catalog.display_books'))

    print("---book_tile-->",book.title)
    print("---book_format-->",book.format)

    return render_template('edit_book.html', form=form)