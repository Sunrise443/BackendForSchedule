from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)

#For plans
def test_add_plan():
  test_data = {
    "user_id": 1,
    "plan_name": "Закончить проект",
    "date": "2025-03-04",
    "completed": False
  }
  response = client.post("/planner/plans", json=test_data)
  assert response.status_code == 200
  assert "plan_id" in response.json() #проверяет наличие ключа в ответе от сервера

def test_all_plan():
  test_data = {
    "user_id": 1,
    "plan_name": "Закончить проект",
    "date": "2025-03-04",
    "completed": False
  }
  post_response = client.post("/planner/plans", json=test_data)
  assert post_response.status_code == 200
  plan_id = post_response.json()["plan_id"]

  response = client.get("/planner/plans")
  assert response.status_code == 200
  assert {**test_data, "id": plan_id} in response.json()

#For goals
def test_add_goal():
  test_data = {
    "user_id": 1,
    "goal_name": "Закончить проект",
    "date": "2025-03-04",
    "completed": False
  }
  response = client.post("/planner/goals", json=test_data)
  assert response.status_code == 200
  assert "goal_id" in response.json()

def test_all_goal():
  test_data = {
    "user_id": 1,
    "goal_name": "Закончить проект",
    "date": "2025-03-04",
    "completed": False
  }
  post_response = client.post("/planner/goals", json=test_data)
  assert post_response.status_code == 200
  goal_id = post_response.json()["goal_id"]

  response = client.get("/planner/goals")
  assert response.status_code == 200
  assert {**test_data, "id": goal_id} in response.json()

#For notes
def test_add_note():
  test_data = {
    "user_id": 1,
    "note_name": "Закончить проект",
    "date": "2025-03-04"
  }
  response = client.post("/planner/notes", json=test_data)
  assert response.status_code == 200
  assert "note_id" in response.json() #проверяет наличие ключа в ответе от сервера

def test_all_note():
  test_data = {
    "user_id": 1,
    "note_name": "Закончить проект",
    "date": "2025-03-04"
  }
  post_response = client.post("/planner/notes", json=test_data)
  assert post_response.status_code == 200
  note_id = post_response.json()["note_id"]

  response = client.get("/planner/notes")
  assert response.status_code == 200
  assert {**test_data, "id": note_id} in response.json()
