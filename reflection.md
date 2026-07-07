# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I designed the system using four main classes: Owner, Pet, Task, and Scheduler. The Owner class stores information about the pet owner, including their available time, preferences, and pets. The Pet class stores information about each pet and its care tasks. The Task class represents activities such as feeding, walking, medication, or grooming, including attributes like duration, priority, and completion status. The Scheduler class is responsible for organizing tasks into a daily schedule based on priorities and the owner’s available time.

The three main actions a user should be able to perform are:
- Add a new pet.
- Schedule a care task for a pet.
- View today's scheduled tasks.

**b. Design changes**

My initial design did not change significantly. After reviewing it, I decided to keep the Scheduler as a separate class instead of putting scheduling logic inside the Owner or Pet classes. This keeps each class focused on a single responsibility and makes the code easier to maintain.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

My scheduler makes a simple tradeoff by only checking for exact time conflicts. For example, it detects if two tasks both start at 09:00, but it does not yet check whether one task overlaps with another based on duration. This is reasonable for the current version because the project only needs lightweight conflict detection, and exact time matching is easier to understand, test, and explain.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
