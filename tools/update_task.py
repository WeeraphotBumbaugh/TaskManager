import requests
from get_task import get_task

BACKEND_URL = "http://127.0.0.1:5000/tasks/"

def update_task(summary, description, is_active, pk):
    task_data = {
        "summary": summary,
        "description": description,
        "is_active": is_active
    }
    url = "%s%s" % (BACKEND_URL, str(pk))
    response = requests.put(url, json=task_data)
    if response.status_code == 204:
        print("Task updated successfully")
        get_task(pk)
    else:
        print("Something went wrong while updating the task")

if __name__ == "__main__":
    print("Update task (interactive mode):")
    summary = input("Enter summary: ")
    description = input("Enter description: ")
    is_active = input("0 for inactive, 1 for active: ")
    pk = input("Enter id: ")
    update_task(summary, description, is_active, pk)