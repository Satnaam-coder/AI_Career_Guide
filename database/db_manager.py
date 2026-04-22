import sqlite3
import os
DB_PATH = "database/career_guide.db"
def get_connection():
    os.makedirs("database", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume_analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_score INTEGER,
        suggested_career TEXT,
        salary_range TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def save_resume_analysis(score, career, salary):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO resume_analysis (resume_score, suggested_career, salary_range)
    VALUES (?, ?, ?)
    """, (score, career, salary))

    conn.commit()
    conn.close()

import bcrypt

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed)
    )

    conn.commit()
    conn.close()


def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return bcrypt.checkpw(password.encode(), result[0])

    return False