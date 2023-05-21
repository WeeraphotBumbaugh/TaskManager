import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks/"

def delete_task(task_id):
    url = BACKEND_URL + str(task_id)
    response = requests.delete(url)
    if response.status_code == 204:
        print("Task deleted successfully")
    else:
        print("Something went wrong while deleting the task")

if __name__ == "__main__":
    task_id = input("Enter task ID to delete: ")
    delete_task(task_id)
