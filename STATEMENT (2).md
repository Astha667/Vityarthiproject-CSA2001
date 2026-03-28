#  Problem Statement

## Project Title
**Movie Recommendation System (Extended Version)**

---

##  Objective

To design and implement a **console-based Movie Recommendation System** in Python that recommends movies to users based on genre similarity — without using any external libraries or built-in sorting functions.

---

##  Problem Description

In today's digital age, users are often overwhelmed by the sheer number of movies available across streaming platforms. A simple, efficient recommendation mechanism can help users discover movies similar to ones they already enjoy.

This project addresses the following problem:

> *"Given a movie that a user likes, how can we programmatically suggest other movies that are most similar to it based on genre overlap?"*

---

##  Scope

### In Scope
- A static movie database stored as a Python dictionary
- Genre-based similarity scoring
- Manual sorting of results (Bubble Sort implementation)
- A menu-driven command-line interface
- Display of top 5 recommendations

### Out of Scope
- User login or profiles
- External database or file storage
- Machine learning or collaborative filtering
- Web or GUI interface

---

##  Functional Requirements

| ID | Requirement |
|----|-------------|
| FR-01 | The system shall display all movies available in the database |
| FR-02 | The system shall accept a movie name as input from the user |
| FR-03 | The system shall validate whether the entered movie exists in the database |
| FR-04 | The system shall compute a match score between the selected movie and all others |
| FR-05 | The system shall sort recommendations in descending order of match score |
| FR-06 | The system shall display the top 5 recommendations with their match scores |
| FR-07 | The system shall provide a looping menu until the user chooses to exit |

---

##  Non-Functional Requirements

| ID | Requirement |
|----|-------------|
| NFR-01 | No external Python libraries shall be used (`import` is not allowed) |
| NFR-02 | Sorting must be implemented manually using a loop-based algorithm |
| NFR-03 | The system must handle invalid movie names gracefully |
| NFR-04 | Code must be readable, modular, and well-commented |

---

##  Algorithm Design

### Match Scoring
For each candidate movie, a score is calculated as:

```
score = number of genres shared with the selected movie
```

### Sorting (Bubble Sort)
Recommendations are sorted in descending order of score using a custom Bubble Sort:

```python
for i in range(len(recommendations)):
    for j in range(i + 1, len(recommendations)):
        if recommendations[j][1] > recommendations[i][1]:
            # swap
            temp = recommendations[i]
            recommendations[i] = recommendations[j]
            recommendations[j] = temp
```

### Output
Only the **top 5** results (by score) are displayed.

---

## 🗃️ Data Design

Movies are stored in a Python dictionary:

```python
movies = {
    "Movie Title": ["Genre1", "Genre2", ...]
}
```

### Current Dataset Summary

| Metric | Value |
|--------|-------|
| Total Movies | 10 |
| Unique Genres | 9 |
| Max Genres per Movie | 3 (Inception) |
| Min Genres per Movie | 2 |

**Genres covered:** Action, Animation, Comedy, Crime, Drama, Family, Romance, Sci-Fi, Thriller

---

##  Test Cases

| Test ID | Input | Expected Output |
|---------|-------|-----------------|
| TC-01 | Movie: `Inception` | Avengers, Interstellar (score ≥ 2) ranked first |
| TC-02 | Movie: `Frozen` | Toy Story (Animation match) recommended |
| TC-03 | Movie: `XYZ` (invalid) | "Movie not found in database!" error message |
| TC-04 | Choice: `3` | Program exits with farewell message |
| TC-05 | Choice: `9` (invalid) | "Invalid choice! Try again." message |

---

##  Learning Outcomes

By completing this project, the developer demonstrates:

1. Use of **Python dictionaries** for structured data storage
2. Implementation of **nested loops** for comparison logic
3. Custom **Bubble Sort** without using built-in functions
4. Modular programming with **functions**
5. **User input handling** and **validation**
6. Building a **menu-driven CLI application**

---

##  Future Enhancements

- Add user ratings per movie
- Load movie data from a CSV or JSON file
- Implement weighted scoring (e.g., primary genre worth more)
- Add a search feature with partial name matching
- Build a GUI or web frontend

---

##  Submitted By

| Field | Details |
|-------|---------|
| Project Type | Academic / Personal Python Project |
| Language | Python 3.x |
| Imports Used | None |
| Difficulty Level | Beginner–Intermediate |
