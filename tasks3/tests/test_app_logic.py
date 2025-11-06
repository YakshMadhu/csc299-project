from tasks3 import app
from pathlib import Path
import json

def test_hash_password_consistency():
	p1 = app.hash_password("abcd123")
	p2 = app.hash_password("abcd123")
	assert p1 == p2
	assert p1 != app.hash_password("different")

def test_save_and_load_user(tmp_path, monkeypatch):
	fake_file = tmp_path / "users.json"
	monkeypatch.setattr(app, "USERS_FILE", fake_file)

	users = {"yaksh": app.hash_password("pass")}
	app.save_users(users)
	loaded = app.load_users()
	assert loaded == users

def test_save_and_load_tasks(tmp_path, monkeypatch):
	def fake_get_task_file(username: str) -> Path:
		return tmp_path / f"tasks_{username}.json"

	monkeypatch.setattr(app, "get_task_file", fake_get_task_file)

	username = "yaksh"
	tasks_in = [
		{"task": "Sketch portrait", "time": "2025-11-05 01:23 PM", "hidden": False}, 
		{"task": "Study composition", "time": "2025-11-05 02:00 PM", "hidden": True}
	]
	app.save_tasks(username, tasks_in)
	tasks_out = app.load_tasks(username)
	assert tasks_out == tasks_in

