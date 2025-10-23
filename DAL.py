import os
import sqlite3
from typing import List, Dict, Optional, Tuple


# Allow overriding the DB path via environment variable so containers can persist DBs
DB_PATH = os.environ.get('PROJECTS_DB_PATH', 'projects.db')


def get_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str = DB_PATH) -> None:
    conn = get_connection(db_path)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                image_file_name TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def insert_project(title: str, description: str, image_file_name: str, db_path: str = DB_PATH) -> int:
    conn = get_connection(db_path)
    try:
        cur = conn.execute(
            "INSERT INTO projects (title, description, image_file_name) VALUES (?, ?, ?)",
            (title, description, image_file_name),
        )
        conn.commit()
        return int(cur.lastrowid)
    finally:
        conn.close()


def fetch_projects(db_path: str = DB_PATH) -> List[Dict]:
    conn = get_connection(db_path)
    try:
        cur = conn.execute(
            "SELECT id, title, description, image_file_name, created_at FROM projects ORDER BY created_at DESC, id DESC"
        )
        rows = cur.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


