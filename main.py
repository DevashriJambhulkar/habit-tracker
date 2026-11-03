from datetime import date, timedelta

from habit import Habit

from analytics import (
    get_current_habits,
    get_habits_by_periodicity,
    get_longest_streak,
    get_longest_streak_overall
)

from storage import save_habits, load_habits

habits = load_habits()

if len(habits) == 0:
    habit1 = Habit("Drink Water", "daily")
    habit2 = Habit("Exercise", "daily")
    habit3 = Habit("Clean Room", "weekly")
    habit4 = Habit("Read Book", "daily")
    habit5 = Habit("Laundry", "weekly")

    habits.append(habit1)
    habits.append(habit2)
    habits.append(habit3)
    habits.append(habit4)
    habits.append(habit5)

    start_date = date(2026, 9, 7)

    for day_number in range(28):
        current_date = start_date + timedelta(days=day_number)
        habit1.add_completion_date(current_date)

    exercise_dates = [
        date(2026, 9, 7),
        date(2026, 9, 8),
        date(2026, 9, 9),
        date(2026, 9, 10),
        date(2026, 9, 12),
        date(2026, 9, 13),
        date(2026, 9, 14),
        date(2026, 9, 16),
        date(2026, 9, 17),
        date(2026, 9, 18),
    ]

    for completion_date in exercise_dates:
        habit2.add_completion_date(completion_date)

    clean_room_dates = [
        date(2026, 9, 7),
        date(2026, 9, 14),
        date(2026, 9, 21),
        date(2026, 9, 28),
    ]

    for completion_date in clean_room_dates:
        habit3.add_completion_date(completion_date)

    save_habits(habits)


def show_habits():
    """Display all currently tracked habits."""

    current_habits = get_current_habits(habits)

    print()
    print("Currently tracked habits:")

    for number, habit in enumerate(current_habits, start=1):
        print(
            number,
            "-",
            habit.name,
            "(",
            habit.periodicity,
            ")"
        )


def create_habit():
    """Create and save a new habit."""

    print()
    print("Create a new habit")

    name = input("Enter habit name: ")

    periodicity = input(
        "Enter periodicity (daily/weekly): "
    ).lower()

    if periodicity != "daily" and periodicity != "weekly":
        print("Invalid periodicity.")
        print("Please use daily or weekly.")
        return

    new_habit = Habit(name, periodicity)

    habits.append(new_habit)

    save_habits(habits)

    print()
    print("Habit created successfully!")
    print("Name:", new_habit.name)
    print("Periodicity:", new_habit.periodicity)


def delete_habit():
    """Delete and save the updated habits."""

    print()
    print("Delete a habit")

    if len(habits) == 0:
        print("There are no habits to delete.")
        return

    for number, habit in enumerate(habits, start=1):
        print(number, "-", habit.name)

    choice = input(
        "Enter the number of the habit to delete: "
    )

    if not choice.isdigit():
        print("Please enter a number.")
        return

    number = int(choice)

    if number < 1 or number > len(habits):
        print("Invalid habit number.")
        return

    deleted_habit = habits.pop(number - 1)

    save_habits(habits)

    print()
    print("Habit deleted:", deleted_habit.name)


def complete_habit():
    """Mark a selected habit as completed."""

    print()
    print("Complete a habit")

    if len(habits) == 0:
        print("There are no habits to complete.")
        return

    for number, habit in enumerate(habits, start=1):
        print(number, "-", habit.name)

    choice = input(
        "Enter the number of the habit to complete: "
    )

    if not choice.isdigit():
        print("Please enter a number.")
        return

    number = int(choice)

    if number < 1 or number > len(habits):
        print("Invalid habit number.")
        return

    selected_habit = habits[number - 1]

    selected_habit.complete_habit()

    save_habits(habits)

    print()
    print("Habit completed:", selected_habit.name)
    print("Completed at:", selected_habit.completed_at)


def show_analytics():
    """Display habit analytics."""

    print()
    print("Habit Analytics:")

    print()
    print("Daily habits:")

    daily_habits = get_habits_by_periodicity(
        habits,
        "daily"
    )

    for habit in daily_habits:
        print("-", habit.name)

    print()
    print("Weekly habits:")

    weekly_habits = get_habits_by_periodicity(
        habits,
        "weekly"
    )

    for habit in weekly_habits:
        print("-", habit.name)

    print()
    print("Longest streak for each habit:")

    for habit in habits:
        streak = get_longest_streak(habit)

        print(
            "-",
            habit.name,
            ":",
            streak,
            "days"
        )

    print()
    print(
        "Longest streak overall:",
        get_longest_streak_overall(habits),
        "days"
    )


def main():
    """Run the Habit Tracker application."""

    while True:

        print()
        print("===== HABIT TRACKER =====")
        print("1. Show habits")
        print("2. Create habit")
        print("3. Delete habit")
        print("4. Complete habit")
        print("5. Show analytics")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_habits()

        elif choice == "2":
            create_habit()

        elif choice == "3":
            delete_habit()

        elif choice == "4":
            complete_habit()

        elif choice == "5":
            show_analytics()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()