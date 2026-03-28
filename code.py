# ============================================================
# MOVIE RECOMMENDATION SYSTEM (EXTENDED VERSION)
# No imports used
# ============================================================

# Step 1: Movie database
movies = {
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Titanic": ["Romance", "Drama"],
    "Avengers": ["Action", "Sci-Fi"],
    "The Notebook": ["Romance", "Drama"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "The Dark Knight": ["Action", "Crime"],
    "Joker": ["Drama", "Crime"],
    "Frozen": ["Animation", "Family"],
    "Toy Story": ["Animation", "Comedy"],
    "Deadpool": ["Action", "Comedy"]
}


# Step 2: Display all movies
def show_movies():
    print("\n🎬 Available Movies:\n")
    for movie in movies:
        print("-", movie)


# Step 3: Recommendation logic
def recommend(movie_name):
    if movie_name not in movies:
        print("\n❌ Movie not found in database!")
        return

    chosen_genres = movies[movie_name]
    recommendations = []

    # compare with all movies
    for movie in movies:
        if movie != movie_name:
            score = 0

            # count matching genres
            for genre in movies[movie]:
                if genre in chosen_genres:
                    score += 1

            if score > 0:
                recommendations.append([movie, score])

    # Step 4: Sort manually (no imports used)
    for i in range(len(recommendations)):
        for j in range(i + 1, len(recommendations)):
            if recommendations[j][1] > recommendations[i][1]:
                temp = recommendations[i]
                recommendations[i] = recommendations[j]
                recommendations[j] = temp

    # Step 5: Show results
    print("\n Top Recommendations:\n")

    if len(recommendations) == 0:
        print("No similar movies found.")
        return

    count = 0
    for item in recommendations:
        print("👉", item[0], "(Match Score:", item[1], ")")
        count += 1
        if count == 5:
            break


# Step 6: Main menu system
def main():
    while True:
        print("\n==============================")
        print("🎬 MOVIE RECOMMENDER SYSTEM")
        print("==============================")
        print("1. Show Movies")
        print("2. Get Recommendation")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            show_movies()

        elif choice == "2":
            movie_name = input("\nEnter movie name: ")
            recommend(movie_name)

        elif choice == "3":
            print("\n Thank you for using the system!")
            break

        else:
            print("\n⚠ Invalid choice! Try again.")


# Step 7: Run program
main()
