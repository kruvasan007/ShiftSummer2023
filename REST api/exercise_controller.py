from db import get_db


def insert_exercise(name, description, type, complexity):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO exercises(name, description, type, complexity) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, description, type, complexity])
    db.commit()
    return True


def update_exercise(id, name, description, type, complexity):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE exercises SET name = ?, description = ?, type = ?, complexity = ? WHERE id = ?"
    cursor.execute(statement, [name, description, type, complexity, id])
    db.commit()
    return True


def delete_exercise(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM exercises WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT name, description, type, complexity FROM exercises WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_exercises():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT name, description, type, complexity FROM exercises"
    cursor.execute(query)
    return cursor.fetchall()