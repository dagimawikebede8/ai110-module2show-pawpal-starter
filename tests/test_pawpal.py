from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    task = Task("Feed breakfast", "09:00", "Daily")
    task.mark_complete()
    assert task.completed


def test_task_addition():
    pet = Pet("Buddy", "Dog")
    task = Task("Morning walk", "08:00", "Daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_sorting_correctness():
    owner = Owner("Aki")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Night walk", "20:00", "Daily"))
    pet.add_task(Task("Morning walk", "08:00", "Daily"))
    pet.add_task(Task("Lunch feeding", "12:00", "Daily"))

    scheduler = Scheduler(owner)
    schedule = scheduler.get_todays_schedule()

    times = [task.time for pet, task in schedule]
    assert times == ["08:00", "12:00", "20:00"]


def test_daily_recurrence_creates_next_day_task():
    owner = Owner("Aki")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Morning walk", "08:00", "Daily"))

    scheduler = Scheduler(owner)
    scheduler.mark_task_complete("Buddy", "Morning walk")

    assert len(pet.tasks) == 2
    assert pet.tasks[0].completed
    assert pet.tasks[1].due_date == date.today() + timedelta(days=1)


def test_conflict_detection():
    owner = Owner("Aki")
    dog = Pet("Buddy", "Dog")
    cat = Pet("Milo", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    dog.add_task(Task("Feed breakfast", "09:00", "Daily"))
    cat.add_task(Task("Feed breakfast", "09:00", "Daily"))

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "Conflict at 09:00" in conflicts[0]