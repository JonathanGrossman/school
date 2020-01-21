import json
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS
from database import students, existing_skills_count, desired_skills_count, interested_courses_count


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


@app.route('/api/skills-data', methods=['GET'])
def skills_data():
    def existing_skills_loop(skills):
        for type in skills:
            for item in existing_skills_count:
                if type["skill"] == item["name"]:
                    item["count"] += 1
    
    def desired_skills_loop(skills):
        for type in skills:
            for item in desired_skills_count:
                if type["skill"] == item["name"]:
                    item["count"] += 1
    
    def interested_courses_loop(skills):
        for type in skills:
            for item in interested_courses_count:
                if type["skill"] == item["name"]:
                    item["count"] += 1
    

    for i in range(len(students)):
            existing_skills_loop(students[i]["existing_skills"])
            desired_skills_loop(students[i]["desired_skills"])
            interested_courses_loop(students[i]["interested_courses"])
    return jsonify(existing_skills_count, desired_skills_count, interested_courses_count)


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