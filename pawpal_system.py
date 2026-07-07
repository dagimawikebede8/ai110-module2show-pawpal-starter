from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    task_type: str
    time: str
    priority: int
    completed: bool = False

    def mark_complete(self):
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_pets(self):
        return self.pets


class Scheduler:
    def __init__(self):
        self.tasks = []

    def schedule_task(self, pet, task):
        pet.add_task(task)
        self.tasks.append(task)

    def get_today_tasks(self):
        return self.tasks

    def sort_tasks_by_priority(self):
        return sorted(self.tasks, key=lambda task: task.priority)