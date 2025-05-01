import pytest
import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.tasks import load_tasks, save_tasks

TEST_FILE = "test_tasks.json"

@pytest.fixture
def setup_valid_json():
   data = [{"task": "Buy coffee"}, {"task": "Debug code"}]
   with open(TEST_FILE, "w") as f:
      json.dump(data, f)
   yield TEST_FILE
   os.remove(TEST_FILE)

def test_load_tasks_valid(setup_valid_json):
   assert load_tasks(setup_valid_json) == [{"task": "Buy coffee"}, {"task": "Debug code"}]


def test_save_tasks(tmp_path):
   tasks = [{"task": "Clean kitchen"}, {"task": "Buy bread"}]
   file_path = tmp_path / TEST_FILE

   save_tasks(tasks, file_path)

   with open(file_path, "r") as f:
      saved_data = json.load(f)

   assert saved_data == tasks


def test_generate_unique_id():
   
