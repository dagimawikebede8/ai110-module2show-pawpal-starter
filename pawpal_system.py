from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a care task to this pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))
        return all_tasks


class Scheduler:
    def __init__(self, owner):
        """Create a scheduler for one owner."""
        self.owner = owner

    def get_todays_schedule(self):
        """Return today's tasks sorted by time."""
        today = date.today()
        todays_tasks = [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if task.due_date == today
        ]
        return self.sort_by_time(todays_tasks)

    def sort_by_time(self, tasks=None):
        """Sort tasks by their HH:MM time."""
        if tasks is None:
            tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda item: item[1].time)

    def filter_by_pet(self, pet_name):
        """Return tasks for one pet by name."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if pet.name.lower() == pet_name.lower()
        ]

    def filter_by_status(self, completed):
        """Return tasks matching a completion status."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if task.completed == completed
        ]

    def mark_task_complete(self, pet_name, task_description):
        """Mark a task complete and create the next recurring task."""
        for pet, task in self.owner.get_all_tasks():
            if pet.name == pet_name and task.description == task_description:
                task.mark_complete()

                if task.frequency == "Daily":
                    pet.add_task(
                        Task(task.description, task.time, task.frequency, task.due_date + timedelta(days=1))
                    )

                elif task.frequency == "Weekly":
                    pet.add_task(
                        Task(task.description, task.time, task.frequency, task.due_date + timedelta(days=7))
                    )

                return True

        return False

    def detect_conflicts(self):
        """Return warnings for tasks scheduled at the same time."""
        warnings = []
        seen_times = {}

        for pet, task in self.owner.get_all_tasks():
            key = task.time

            if key in seen_times:
                other_pet, other_task = seen_times[key]
                warnings.append(
                    f"Conflict at {task.time}: {other_pet.name}'s {other_task.description} "
                    f"and {pet.name}'s {task.description}"
                )
            else:
                seen_times[key] = (pet, task)

        return warnings