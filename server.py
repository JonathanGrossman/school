import json
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS
from database import students, existing_skills_count, desired_skills_count, interested_courses_count, daily_signup_count, monthly_signup_count
from datetime import datetime


app = Flask(__name__)
CORS(app)


@app.route("/api/add-student", methods=["POST"])
def post_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify({"message": "success"})


@app.route('/api/edit-student/<id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == "POST":
        for student in students:
            if student["id"] == id:
                students.remove(student)
                updated_student =  request.get_json()
                students.append(updated_student)
        return jsonify({"message": "success"})
    else:
        return jsonify({"message": "error"})


@app.route('/api/delete-student/<id>', methods=['GET', 'POST'])
def delete_student(id):
    if request.method == "POST":
        data = request.get_json()
        for student in students:
            if student["id"] == id:
                students.remove(student)
        return jsonify({"message": "success"})
    else:
        return jsonify({"message": "error"})


@app.route("/")
def hello_handler():
    return render_template('index.html')


@app.route("/api/students", methods=["GET"])
def students_handler():
    sorted_students = sorted(students, key=lambda k: k['last_name'])
    return jsonify(sorted_students)


@app.route("/<id>", methods=["GET"])
def single_studentid(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)


@app.route('/api/skills-data', methods=['GET'])
def skills_data():
    for item in existing_skills_count:
        item["count"] = 0
    for item in desired_skills_count:
        item["count"] = 0
    for item in interested_courses_count:
        item["count"] = 0
    def existing_skills_loop(skills):
        for type in skills:
            for item in existing_skills_count:
                if type["skill"] == item["name"]:
                    item["count"] += 1
        return existing_skills_count
    
    def desired_skills_loop(skills):
        for type in skills:
            for item in desired_skills_count:
                if type["skill"] == item["name"]:
                    item["count"] += 1
        return
    
    def interested_courses_loop(skills):
        for type in skills:
            for item in interested_courses_count:
                if type["skill"] == item["name"]:
                    item["count"] += 1
        return
    
    for i in range(len(students)):
        existing_skills_loop(students[i]["existing_skills"])
        desired_skills_loop(students[i]["desired_skills"])
        interested_courses_loop(students[i]["interested_courses"])         
    return jsonify({"existing_skills_count": existing_skills_count}, {"desired_skills_count": desired_skills_count}, {"interested_courses_count": interested_courses_count})


@app.route('/api/signup-counts', methods=['GET'])
def signup_counts():
    global students
    for item in daily_signup_count:
        item["count"] = 0
    for item in monthly_signup_count:
        item["count"] = 0
    def daily_signup_counts_loop(student):
        student_dt_object = datetime.fromtimestamp(student["create_time"])
        if len(daily_signup_count) > 0: 
            for item in daily_signup_count:            
                item_month_object = datetime.fromtimestamp(item["date"])
                if (student_dt_object.day == item_month_object.day and student_dt_object.month == item_month_object.month and student_dt_object.year == item_month_object.year):
                    item["count"] += 1
                    return
        
        new_month = {
            "date": student["create_time"],
            "count": 1
        }
        daily_signup_count.append(new_month)
        return daily_signup_count

    def monthly_signup_counts_loop(student): 
        student_dt_object = datetime.fromtimestamp(student["create_time"])
        if len(monthly_signup_count) > 0: 
            for item in monthly_signup_count:            
                item_month_object = datetime.fromtimestamp(item["date"])
                if (student_dt_object.month == item_month_object.month and student_dt_object.year == item_month_object.year):
                    item["count"] += 1
                    return
        new_month = {
                "date": student["create_time"],
                "count": 1
        }
        monthly_signup_count.append(new_month)
        return monthly_signup_count
    for i in range(len(students)):
        daily_signup_counts_loop(students[i])
        monthly_signup_counts_loop(students[i])      
    return jsonify({"daily_signup_count": daily_signup_count}, {"monthly_signup_count": monthly_signup_count})


if __name__ == "__main__":
    app.run(host="localhost", port=7000, debug=True)