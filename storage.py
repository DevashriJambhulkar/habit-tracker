import json

from datetime import datetime, date

from habit import Habit


FILE_NAME = "habits.json"


def save_habits(habits):
    """Save all habits to a JSON file."""

    data = []

    for habit in habits:
        data.append(habit.to_dict())

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_habits():
    """Load habits from the JSON file."""

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        return []

    habits = []

    for item in data:
        habit = Habit(
            item["name"],
            item["periodicity"]
        )

        habit.created_at = datetime.fromisoformat(
            item["created_at"]
        )

        habit.completed = item["completed"]

        if item["completed_at"]:
            habit.completed_at = datetime.fromisoformat(
                item["completed_at"]
            )

        habit.completion_dates = [
            date.fromisoformat(completion_date)
            for completion_date in item["completion_dates"]
        ]

        habits.append(habit)

    return habits