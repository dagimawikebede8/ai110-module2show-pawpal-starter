# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```text
Today's Schedule
----------------
08:00 - Buddy (Dog): Morning walk [Daily] - Not Done
09:00 - Buddy (Dog): Feed breakfast [Daily] - Not Done
10:30 - Milo (Cat): Clean litter box [Daily] - Not Done
```

## Testing PawPal+

To run the automated tests:

```bash
python3 -m pytest
```

The tests verify task completion, task addition, schedule sorting, daily recurrence, and conflict detection.

Successful test output:

```text
============================= test session starts ==============================
collected 5 items

tests/test_pawpal.py .....                                            [100%]

============================== 5 passed in 0.01s ===============================
```

Confidence Level: ⭐⭐⭐⭐☆  
I am fairly confident because the main class behaviors and scheduling algorithms pass automated tests, but more edge cases could still be added later.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts tasks by their `HH:MM` time value. |
| Filtering by pet | `Scheduler.filter_by_pet()` | Shows only tasks for a selected pet. |
| Filtering by status | `Scheduler.filter_by_status()` | Shows completed or incomplete tasks. |
| Conflict detection | `Scheduler.detect_conflicts()` | Warns when two tasks share the same exact time. |
| Recurring tasks | `Scheduler.mark_task_complete()` | Creates the next daily or weekly task after completion. |

## 📸 Demo Walkthrough

PawPal+ allows a user to enter owner information, add pets, add care tasks, and view a daily schedule. The app uses the backend `Scheduler` class to sort tasks by time and warn the user when two tasks are scheduled at the same time.

Example workflow:

1. Enter the owner name.
2. Add a pet with a name and species.
3. Add a task for that pet with a description, time, and frequency.
4. View the generated schedule under "Today's Schedule."
5. If two tasks happen at the same time, the app displays a conflict warning.

Sample CLI output from `main.py`:

```text
Today's Schedule
----------------
08:00 - Buddy (Dog): Morning walk [Daily] - Not Done
09:00 - Buddy (Dog): Feed breakfast [Daily] - Not Done
09:00 - Milo (Cat): Feed breakfast [Daily] - Not Done
10:30 - Milo (Cat): Clean litter box [Daily] - Not Done

Tasks for Buddy
---------------
09:00 - Buddy: Feed breakfast
08:00 - Buddy: Morning walk

Incomplete Tasks
----------------
09:00 - Buddy: Feed breakfast
08:00 - Buddy: Morning walk
10:30 - Milo: Clean litter box
09:00 - Milo: Feed breakfast

Conflicts
---------
Conflict at 09:00: Buddy's Feed breakfast and Milo's Feed breakfast

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
