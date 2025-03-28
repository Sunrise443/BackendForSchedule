import pytest
from httpx import ASGITransport, AsyncClient

from app.api import app



#For plans
@pytest.mark.asyncio
async def test_add_plan():
  client = AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
  test_data = {
    "user_id": 1,
    "plan_name": "Закончить проект",
    "date": "2025-03-04",
    "completed": False
  }
  async with client:
    response = await client.post("/planner/plans", json=test_data)
  assert response.status_code == 200
  assert "plan_id" in response.json() #проверяет наличие ключа в ответе от сервера

@pytest.mark.asyncio
async def test_all_plan():
  client = AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
  test_data = {
    "user_id": 1,
    "plan_name": "Закончить проект",
    "date": "2025-03-04",
    "completed": False
  }
  async with client:
    post_response = await client.post("/planner/plans", json=test_data)
    plan_id = post_response.json()["plan_id"]
    response = await client.get("/planner/plans")

  assert post_response.status_code == 200
  assert response.status_code == 200
  assert {**test_data, "id": plan_id} in response.json()

#For goals
@pytest.mark.asyncio
async def test_add_goal():
  client = AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
  test_data = {
    "user_id": 1,
    "goal_name": "Закончить проект",
    "date": "2025-03-04",
    "completed": False
  }
  async with client:
    response = await client.post("/planner/goals", json=test_data)
  assert response.status_code == 200
  assert "goal_id" in response.json()

@pytest.mark.asyncio
async def test_all_goal():
  client = AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
  test_data = {
    "user_id": 1,
    "goal_name": "Закончить проект",
    "date": "2025-03-04",
    "completed": False
  }
  async with client:
    post_response = await client.post("/planner/goals", json=test_data)
    goal_id = post_response.json()["goal_id"]
    response = await client.get("/planner/goals")
  
  assert post_response.status_code == 200
  assert response.status_code == 200
  assert {**test_data, "id": goal_id} in response.json()

#For notes
@pytest.mark.asyncio
async def test_add_note():
  client = AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
  test_data = {
    "user_id": 1,
    "note_name": "Закончить проект",
    "date": "2025-03-04"
  }
  async with client:
    response = await client.post("/planner/notes", json=test_data)
  assert response.status_code == 200
  assert "note_id" in response.json() #проверяет наличие ключа в ответе от сервера

@pytest.mark.asyncio
async def test_all_note():
  client = AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
  test_data = {
    "user_id": 1,
    "note_name": "Закончить проект",
    "date": "2025-03-04"
  }
  async with client:
    post_response = await client.post("/planner/notes", json=test_data)
    note_id = post_response.json()["note_id"]
    response = await client.get("/planner/notes")

  assert post_response.status_code == 200
  assert response.status_code == 200
  assert {**test_data, "id": note_id} in response.json()
