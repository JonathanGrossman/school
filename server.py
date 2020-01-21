import json
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS
from database import students, existing_skills_count, desired_skills_count, interested_courses_count, daily_signup_count, monthly_signup_count
from datetime import datetime

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
            
    return jsonify({"existing_skills_count": existing_skills_count}, {"desired_skills_count": desired_skills_count}, {"interested_courses_count": interested_courses_count})


@app.route('/api/signup-counts', methods=['GET'])
def signup_counts():
    def daily_signup_counts_loop(student):
        if len(daily_signup_count) > 0:
            for item in daily_signup_count:
                student_day_object = datetime.fromtimestamp(student["create_time"])
                item_day_object = datetime.fromtimestamp(item["date"])
                if (student_day_object.day == item_day_object.day):
                    item["count"] += 1
                    return
                else: 
                    new_day = {
                        "date": student["create_time"],
                        "count": 1
                    }
                    return daily_signup_count.append(new_day)
        else:
            new_day = {
                "date": student["create_time"],
                "count": 1
            }
            return daily_signup_count.append(new_day)

    def monthly_signup_counts_loop(student): 
        if len(monthly_signup_count) > 0: 
            for item in monthly_signup_count:            
                student_month_object = datetime.fromtimestamp(student["create_time"])
                item_month_object = datetime.fromtimestamp(item["date"])
                if (student_month_object.month == item_month_object.month):
                    item["count"] += 1
                    return
                else: 
                    new_month = {
                        "date": student["create_time"],
                        "count": 1
                    }
                    return monthly_signup_count.append(new_month)
        else:
            new_month = {
                "date": student["create_time"],
                    "count": 1
            }
            return monthly_signup_count.append(new_month)

    for i in range(len(students)):
        daily_signup_counts_loop(students[i])
        monthly_signup_counts_loop(students[i])

            
    return jsonify({"daily_signup_count": daily_signup_count}, {"monthly_signup_count": monthly_signup_count})


if __name__ == "__main__":
    app.run(host="localhost", port=7000, debug=True)