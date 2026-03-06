"""Add several todos to todo service.

Run this as a Python script to create todos in the running service.
The service URL and API_ROOT are defined in config.py.
"""

from datetime import datetime
import time

from config import ROOT_PATH
from conftest import _SimpleClient, BASE_URL


def now():
    """Current datetime as a string."""
    return str(datetime.now())


def create_todo(client):
    """POST {ROOT_PATH}/todos should create a new todo and return Location header."""
    new_todo = {"text": f"Test create todo {now()}", "done": False}
    response = client.post(f"{ROOT_PATH}/todos/", json=new_todo)
    assert response.status_code == 201
    location = response.headers.get("location")
    assert location is not None
    # The todo id should be last element in the location
    todo_id = location.rstrip("/").rsplit("/", 1)[-1]
    return todo_id


def main():
    number_to_create = 20
    client = _SimpleClient(BASE_URL)
    print(f"Creating {number_to_create} todos")
    print("Todo IDs: ", end="", flush=True)
    for n in range(number_to_create):
        time.sleep(0.05)  # Sleep to ensure different timestamps
        todo_id = create_todo(client)
        print(f"{todo_id}  ", end="", flush=True)

    print("\nDone.")
   

if __name__ == '__main__':
    main()
