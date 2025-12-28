from models.task_model import create_task, get_tasks, update_task, delete_task

def service_get_all_tasks():
    return get_tasks()

def service_create_task(data):
    return create_task(data["title"], data["description"], data["status"])

def service_update_task(task_id, data):
    update_task(task_id, data["title"], data["description"], data["status"])

def service_delete_task(task_id):
    delete_task(task_id)
