import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

st.subheader("Owner Info")

owner_name = st.text_input("Owner name", value=st.session_state.owner.name)

if st.button("Save owner name"):
    st.session_state.owner.name = owner_name
    st.success(f"Owner saved: {owner_name}")

st.divider()

st.subheader("Add a Pet")

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    new_pet = Pet(pet_name, species)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added {pet_name}!")

st.divider()

st.subheader("Pets")

if st.session_state.owner.pets:
    for pet in st.session_state.owner.pets:
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets added yet.")

st.divider()

st.subheader("Add a Task")

if st.session_state.owner.pets:
    pet_names = [pet.name for pet in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Choose pet", pet_names)

    task_description = st.text_input("Task description", value="Morning walk")
    task_time = st.text_input("Task time", value="08:00")
    task_frequency = st.selectbox("Frequency", ["Daily", "Weekly", "One-time"])

    if st.button("Add task"):
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet_name:
                new_task = Task(task_description, task_time, task_frequency)
                pet.add_task(new_task)
                st.success(f"Added task for {pet.name}!")
else:
    st.info("Add a pet before adding tasks.")

st.divider()

st.subheader("Today's Schedule")

scheduler = Scheduler(st.session_state.owner)
schedule = scheduler.get_todays_schedule()
conflicts = scheduler.detect_conflicts()

if conflicts:
    st.warning("Task conflict detected!")
    for conflict in conflicts:
        st.write(conflict)

if schedule:
    schedule_rows = []

    for pet, task in schedule:
        status = "Done" if task.completed else "Not Done"
        schedule_rows.append(
            {
                "Time": task.time,
                "Pet": pet.name,
                "Species": pet.species,
                "Task": task.description,
                "Frequency": task.frequency,
                "Status": status,
            }
        )

    st.table(schedule_rows)
else:
    st.info("No tasks scheduled yet.")