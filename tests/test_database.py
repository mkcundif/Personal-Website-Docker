import os
import tempfile
import sqlite3
from DAL import init_db, insert_project, fetch_projects, DB_PATH, get_connection


def test_init_db_creates_file_and_table(tmp_path):
    db_file = tmp_path / "test_projects.db"
    db_path = str(db_file)

    # Initialize a new DB at the path
    init_db(db_path)

    assert os.path.exists(db_path)

    # Check that the projects table exists
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects';")
        row = cur.fetchone()
        assert row is not None
    finally:
        conn.close()


def test_insert_and_fetch_projects(tmp_path):
    db_file = tmp_path / "test_projects2.db"
    db_path = str(db_file)

    # init
    init_db(db_path)

    # insert two projects
    id1 = insert_project("Title 1", "Desc 1", "img1.png", db_path=db_path)
    id2 = insert_project("Title 2", "Desc 2", "img2.png", db_path=db_path)

    assert isinstance(id1, int)
    assert isinstance(id2, int)

    projects = fetch_projects(db_path=db_path)
    assert len(projects) == 2
    titles = {p['title'] for p in projects}
    assert "Title 1" in titles and "Title 2" in titles
