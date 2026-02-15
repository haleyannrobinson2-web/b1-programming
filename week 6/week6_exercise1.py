# Music Library Manager

# Step 1: Create empty data structures
songs = []
genre_count = {}

print("Welcome to Music Library Manager!\n")

# Step 2 & 3: Collect 5 songs and store information
for i in range(1, 6):
    print(f"Enter Song {i}:")
    song_name = input("  Song name: ")
    genre = input("  Genre: ")

    # Store as a tuple and append to the list
    songs.append((song_name, genre))

    # Count genres in the dictionary
    genre_count[genre] = genre_count.get(genre, 0) + 1
    print()  # Blank line for readability

# Step 4: Display Results

# Display complete song list
print("=== YOUR MUSIC LIBRARY ===")
for idx, (name, genre) in enumerate(songs, start=1):
    print(f"{idx}. {name} ({genre})")

# Display genre statistics
print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} song{'s' if count > 1 else ''}")

# Identify the most popular genre
most_popular = max(genre_count, key=genre_count.get)
print(f"Most popular genre: {most_popular}")
