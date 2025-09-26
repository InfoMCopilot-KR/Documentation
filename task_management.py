from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task:
    def __init__(self, title, description=""):
        self.id = id(self)
        self.title = title
        self.description = description
        self.status = TaskStatus.PENDING
        self.created_at = datetime.now()
        self.completed_at = None


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        # Add implementation here
        pass

    def complete_task(self, task_id):
        # Add implementation here
        pass

    def get_pending_tasks(self):
        # Add implementation here
        pass


if __name__ == "__main__":
    # Basic demo
    manager = TaskManager()
    task = Task("Learn GitHub Copilot", "Practice with prompts")
    print(f"Created task: {task.title}")
    print(f"Status: {task.status.value}")
