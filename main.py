from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Aki")

dog = Pet("Buddy", "Dog")
cat = Pet("Milo", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

dog.add_task(Task("Morning walk", "08:00", "Daily"))
dog.add_task(Task("Feed breakfast", "09:00", "Daily"))
cat.add_task(Task("Clean litter box", "10:30", "Daily"))

scheduler = Scheduler(owner)
schedule = scheduler.get_todays_schedule()

print("Today's Schedule")
print("----------------")

for pet, task in schedule:
    status = "Done" if task.completed else "Not Done"
    print(f"{task.time} - {pet.name} ({pet.species}): {task.description} [{task.frequency}] - {status}")