from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Feed breakfast", "09:00", "Daily")
    task.mark_complete()
    assert task.completed


def test_task_addition():
    pet = Pet("Buddy", "Dog")
    task = Task("Morning walk", "08:00", "Daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1