import json
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS


books = [
            {   
                "id": "1",
                "title": "Book One",
                "author": "Juan Solo",
                "pages": "100"
            },
            {
                "id": "2",
                "title": "The First Sequel",
                "author": "Duo Double",
                "pages": "200"
            },
            {
                "id": "3",
                "title": "Number Three",
                "author": "Thria Threaded",
                "pages": "300"
            },
            {
                "id": "4",
                "title": "What comes after three?",
                "author": "Arba",
                "pages": "400"
            },
            {   
                "id": "5",
                "title": "Book One",
                "author": "Juan Solo",
                "pages": "100"
            },
            {
                "id": "6",
                "title": "The First Sequel",
                "author": "Duo Double",
                "pages": "200"
            },
            {
                "id": "7",
                "title": "Number Three",
                "author": "Thria Threaded",
                "pages": "300"
            },
            {
                "id": "8",
                "title": "What comes after three?",
                "author": "Arba",
                "pages": "400"
            },
            {   
                "id": "9",
                "title": "Book One",
                "author": "Juan Solo",
                "pages": "100"
            },
            {
                "id": "10",
                "title": "The First Sequel",
                "author": "Duo Double",
                "pages": "200"
            },
            {
                "id": "11",
                "title": "Number Three",
                "author": "Thria Threaded",
                "pages": "300"
            },
            {
                "id": "12",
                "title": "What comes after three?",
                "author": "Arba",
                "pages": "400"
            },
            {   
                "id": "13",
                "title": "Book One",
                "author": "Juan Solo",
                "pages": "100"
            },
            {
                "id": "14",
                "title": "The First Sequel",
                "author": "Duo Double",
                "pages": "200"
            },
            {
                "id": "15",
                "title": "Number Three",
                "author": "Thria Threaded",
                "pages": "300"
            },
            {
                "id": "16",
                "title": "What comes after three?",
                "author": "Arba",
                "pages": "400"
            },
            {   
                "id": "17",
                "title": "Book One",
                "author": "Juan Solo",
                "pages": "100"
            },
            {
                "id": "18",
                "title": "The First Sequel",
                "author": "Duo Double",
                "pages": "200"
            },
            {
                "id": "19",
                "title": "Number Three",
                "author": "Thria Threaded",
                "pages": "300"
            },
            {
                "id": "20",
                "title": "What comes after three?",
                "author": "Arba",
                "pages": "400"
            },
            {   
                "id": "21",
                "title": "Book One",
                "author": "Juan Solo",
                "pages": "100"
            },
            {
                "id": "22",
                "title": "The First Sequel",
                "author": "Duo Double",
                "pages": "200"
            },
            {
                "id": "23",
                "title": "Number Three",
                "author": "Thria Threaded",
                "pages": "300"
            },
            {
                "id": "24",
                "title": "What comes after three?",
                "author": "Arba",
                "pages": "400"
            }
        ]


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_handler():
    return render_template('index.html', books=books)

@app.route("/api/books")
def books_handler():
    return jsonify(books)

@app.route("/api/post", methods=["POST"])
def post_book():
    data =  request.get_json()
    books.append(data)
    return redirect(url_for("hello_handler"))

@app.route("/<id>", methods=["GET", "DELETE"])
def single_bookid(id):
    if request.method == "DELETE":
        # DELETE
        return "delete"
    else:
        for book in books:
            if book["id"] == id:
                return render_template('book.html', book=book)

@app.route("/add-book/", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "id": str(len(books)+1),
            "title": request.form["title"], 
            "author": request.form["author"], 
            "pages": request.form["pages"]
            }  
        books.append(book)
        return redirect(url_for("hello_handler"))
    else:
        return render_template("addbook.html")

@app.route('/edit-book/<id>', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == "POST":
        for book in books:
            if book["id"] == id:
                books.remove(book)
                updated_book = {
                    "id": str(id),
                    "title": request.form["title"], 
                    "author": request.form["author"], 
                    "pages": request.form["pages"]
                    }  
                books.append(updated_book)
        return redirect(url_for("hello_handler"))
    else:
        return render_template("editbook.html")


@app.route('/delete-book/<id>', methods=['GET', 'POST'])
def delete_book(id):
    if request.method == "POST":
        for book in books:
            if book["id"] == id:
                if book["title"] == request.form["title"]:
                    books.remove(book)
        return redirect(url_for("hello_handler"))
    else:
        return render_template("deletebook.html")

#endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        results_books = []
        search_input = request.form['book']
        for b in books:
            if b["author"].find(search_input) != -1 or b["title"].find(search_input) != -1:
                if len(results_books) < 5:
                    results_books.append(b)
        return render_template('search.html', data=results_books), 200

    if request.method == "GET":
        return render_template('search.html', data=books), 200

if __name__ == "__main__":
    app.run(host="localhost", port=7000, debug=True)