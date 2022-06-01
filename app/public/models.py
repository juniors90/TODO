from app.firestore_service import db

class Task:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"<Task of {self.user_id}>"
    
    def save_task(self, task, done, state):
        user_data_task = db.collection("users")\
            .document(self.user_id)\
            .collection("todos")
        return user_data_task.add({
            'task': task,
            'done': done,
            'state': state
        })
    
    def delete_task(self, task_id):
        user_data_task = self.get_task_ref(task_id=task_id)
        return user_data_task.delete()
    
    def update_task(self, task_id, task, done, state):
        user_data_task = self.get_task_ref(task_id=task_id)
        return user_data_task.update({
            'task': task,
            'done': done,
            'state': state
        })
    
    def get_task_ref(self, task_id):
        return db.collection("users").document(self.user_id).collection("todos").document(task_id)
    
    def get_task_to_dict(self, task_id):
        task_ref = db.collection("users")\
            .document(self.user_id)\
            .collection("todos")\
            .document(task_id)\
            .get()
        return task_ref.to_dict()
