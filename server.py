import json
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS


students = [
            {   
                "id": "1",
                "first_name": "Book One",
                "last_name": "Juan Solo",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "2",
                "first_name": "The First Sequel",
                "last_name": "Duo Double",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "3",
                "first_name": "Number Three",
                "last_name": "Thria Threaded",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "4",
                "first_name": "What comes after three?",
                "last_name": "Arba",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {   
                "id": "5",
                "first_name": "Book One",
                "last_name": "Juan Solo",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "6",
                "first_name": "The First Sequel",
                "last_name": "Duo Double",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "7",
                "first_name": "Number Three",
                "last_name": "Thria Threaded",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "8",
                "first_name": "What comes after three?",
                "last_name": "Arba",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {   
                "id": "9",
                "first_name": "Book One",
                "last_name": "Juan Solo",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "10",
                "first_name": "The First Sequel",
                "last_name": "Duo Double",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "11",
                "first_name": "Number Three",
                "last_name": "Thria Threaded",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            },
            {
                "id": "12",
                "first_name": "What comes after three?",
                "last_name": "Arba",
                "existing_skills": [{"skill": "Alchemy", "level": "1"}],
                "desired_skills": [{"skill": "Alchemy", "level": "1"}],
                "interested_courses": [{"skill": "Alchemy basics", "level": "1"}]
            }
        ]


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_handler():
    return render_template('index.html', students=students)

@app.route("/api/students", methods=["GET"])
def students_handler():
    return jsonify(students)

@app.route("/api/add-student", methods=["POST"])
def post_book():
    return jsonify({"message": "suceess"})

@app.route('/api/edit-student/<id>', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == "POST":
        for student in students:
            if student["id"] == id:
                students.remove(student)
                data =  request.get_json()
                students.append(data)
        return jsonify({"message": "suceess"})
    else:
        return jsonify({"message": "error"})


@app.route('/api/delete-student/<id>', methods=['GET', 'POST'])
def delete_book(id):
    if request.method == "POST":
        data =  request.get_json()
        for student in students:
            if student["id"] == id:
                if student["first_name"] == data["first_name"]:
                    students.remove(student)
        return jsonify({"message": "suceess"})
    else:
        return jsonify({"message": "error"})


@app.route("/<id>", methods=["GET"])
def single_bookid(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)


# #endpoint for search
# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == "POST":
#         results_students = []
#         search_input = request.form['book']
#         for b in students:
#             if b["last_name"].find(search_input) != -1 or b["first_name"].find(search_input) != -1:
#                 if len(results_students) < 5:
#                     results_students.append(b)
#         return render_template('search.html', data=results_students), 200

#     if request.method == "GET":
#         return render_template('search.html', data=students), 200

if __name__ == "__main__":
    app.run(host="localhost", port=7000, debug=True)