from flask import Flask, jsonify, request

import exercise_controller
from db import create_tables

app = Flask(__name__)

@app.route('/exercises', methods=["GET"])
def get_exercises():
    exercises = exercise_controller.get_exercises()
    return jsonify(exercises)

@app.route("/exercise", methods=["POST"])
def insert_exercise():
    exercise_details = request.get_json()
    name = exercise_details["name"]
    description = exercise_details["description"]
    type = exercise_details["type"]
    complexity = exercise_details["complexity"]
    result = exercise_controller.insert_exercise(name, description, type, complexity)
    return jsonify(result)


@app.route("/exercise", methods=["PUT"])
def update_exercise():
    exercise_details = request.get_json()
    id = exercise_details["id"]
    name = exercise_details["name"]
    description = exercise_details["description"]
    type = exercise_details["type"]
    complexity = exercise_details["complexity"]
    result = exercise_controller.update_exercise(id, name, description, type, complexity)
    return jsonify(result)

@app.route("/exercise/<id>", methods=["DELETE"])
def delete_exercise(id):
    result = exercise_controller.delete_exercise(id)
    return jsonify(result)

@app.route("/exercise/<id>", methods=["GET"])
def get_exercise_by_id(id):
    exercise = exercise_controller.get_by_id(id)
    return jsonify(exercise)


if __name__ == "__main__":
    create_tables()
    app.run(port=8000, debug=False)