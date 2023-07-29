date = input("Enter today's date: ")
# mood = input("How do you rate your mood today, 1 to 10? ")
thoughts = input("Let your mind flow: \n")

file_path = f"journal-entries/{date}.txt"

with open(file_path, "w") as file:
    file.write(f"Date: {date}\n")
    # file.write(f"Mood: {mood}\n")
    file.write(f"Thoughts:\n")
    file.write(thoughts)
    