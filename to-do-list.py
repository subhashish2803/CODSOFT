def display_menu():
    print("Menu:")
    print("1. Add the exercise")
    print("2. View the exercise")
    print("3. Mark as Done befoe")
    print("4. Exit")


def add_exercise(exercise):
    exercise = input("Enter exercise description: ")
    exercise.append(exercise)
    print("exercise added successfully!")


def view_exercise(exercise):
    print("\nexercise:")
    for i, exercise in enumerate(exercise, start=1):
        print(f"{i}. {task}")


def mark_exercise_done(exercise):
    if not exercise:
        print("No exercise to mark as done yet.")
        return


    view_exercise(exercise)
    index = int(input("Enter exercise index to mark as done: ")) - 1


    if 0 <= index < len(exercise):
        removed_exercise = exercise.pop(index)
        print(f"exercise '{removed_exercise}' marked as done and removed.")
    else:
        print("Invalid exercise index.")


def save_exercise(exercise):
    with open("exercise.txt", "w") as f:
        for exercise in exercise:
            f.write(exercise + '\n')


def load_exercise():
    try:
        with open("exercise.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def main():
    exercise = load_exercise()


    while True:
        display_menu()


        choice = input("Enter your choice: ")


        if choice == '1':
            add_exercise(exercise)
        elif choice == '2':
            view_exercise(exercise)
        elif choice == '3':
            mark_exercise_done(exercise)
        elif choice == '4':
            print("Exiting.")
            save_exercise(exercise)
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()