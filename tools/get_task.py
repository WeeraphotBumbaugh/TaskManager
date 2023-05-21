import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks/"

def get_task(task_id):
    url = BACKEND_URL + str(task_id)
    response = requests.get(url)
    if response.status_code == 200:
        task_data = response.json()
        print("---Task details---")
        print("ID:", task_data["task"]["id"])
        print("Summary:", task_data["task"]["summary"])
        print("Description:", task_data["task"]["description"])
        print("Is Active:", task_data["task"]["is_active"])
    else:
        print("Error occurred while fetching the task")

if __name__ == "__main__":
    task_id = input("Enter task ID to retrieve: ")
    get_task(task_id)
