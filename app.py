from flask import Flask, request, jsonify
from models import db, Book
import os

app = Flask(__name__, static_folder='static', static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def serve_ui():
    return app.send_static_file("index.html")


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify([b.to_dict() for b in Book.query.all()])

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    book = Book(title=data["title"], author=data["author"], year=data["year"])
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return {"error": "Not found"}, 404
    data = request.json
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.year = data.get("year", book.year)
    db.session.commit()
    return jsonify(book.to_dict())

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return {"error": "Not found"}, 404
    db.session.delete(book)
    db.session.commit()
    return '', 204

@app.route("/books/delete_all", methods=["DELETE"])
def delete_all_books():
    Book.query.delete()
    db.session.commit()
    return '', 204

if __name__ == "__main__":
    app.run(debug=True, port=5001)
