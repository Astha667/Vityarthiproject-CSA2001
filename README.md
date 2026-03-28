# Vityarthiproject-CSA2001
#  Movie Recommendation System

A lightweight, Python-based command-line movie recommendation engine that suggests similar movies based on shared genres — built with **zero external imports**.

---

##  Overview

This system allows users to browse a curated movie database and receive personalized recommendations based on genre similarity. Each recommendation is ranked using a custom match-scoring algorithm implemented entirely in pure Python.

---

##  Features

-  View all available movies in the database
-  Get top 5 genre-based movie recommendations
-  Custom sorting algorithm (no `sorted()` or `import` used)
-  Match scoring based on overlapping genres
-  Simple and intuitive menu-driven interface

---

##  Project Structure

```
movie-recommender/
│
├── movie_recommender.py   # Main application file
├── README.md              # Project documentation
├── STATEMENT.md           # Problem statement & objectives
└── movies.csv             # Movie database export
```

---

##  How to Run

### Prerequisites
- Python 3.x installed
- No additional libraries required

### Steps

```bash
# Clone or download the project
git clone https://github.com/yourname/movie-recommender.git

# Navigate to the project folder
cd movie-recommender

# Run the script
python movie_recommender.py
```

---

## 📖 Usage

When the program launches, you'll see a menu:

```
==============================
🎬 MOVIE RECOMMENDER SYSTEM
==============================
1. Show Movies
2. Get Recommendation
3. Exit
```

- **Option 1** — Lists all movies in the database
- **Option 2** — Enter a movie name to get up to 5 similar recommendations
- **Option 3** — Exit the program

### Example

```
Enter movie name: Inception

 Top Recommendations:

👉 Avengers (Match Score: 2)
👉 Interstellar (Match Score: 2)
👉 The Dark Knight (Match Score: 1)
👉 Deadpool (Match Score: 1)
👉 Joker (Match Score: 1)
```

---

##  Movie Database

| Movie | Genres |
|---|---|
| Inception | Sci-Fi, Action, Thriller |
| Titanic | Romance, Drama |
| Avengers | Action, Sci-Fi |
| The Notebook | Romance, Drama |
| Interstellar | Sci-Fi, Drama |
| The Dark Knight | Action, Crime |
| Joker | Drama, Crime |
| Frozen | Animation, Family |
| Toy Story | Animation, Comedy |
| Deadpool | Action, Comedy |

---

## How It Works

1. User selects a movie
2. System retrieves its genre list
3. Each other movie is scored by counting shared genres
4. Results are sorted using **Bubble Sort** (no imports)
5. Top 5 matches are displayed

---

##  Constraints

-  No external libraries used
-  No `import` statements
-  Pure Python logic only

---

##  License

This project is open-source and free to use for educational purposes.

---

## Author

Developed as a beginner-friendly Python project demonstrating core programming concepts: dictionaries, loops, functions, and sorting algorithms.
