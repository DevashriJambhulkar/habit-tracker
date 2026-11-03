from datetime import timedelta


def get_current_habits(habits):
    """Return all currently tracked habits."""
    return list(habits)


def get_habits_by_periodicity(habits, periodicity):
    """Return habits matching the given periodicity."""
    return [
        habit
        for habit in habits
        if habit.periodicity == periodicity
    ]


def get_longest_streak(habit):
    """Return the longest consecutive-day streak for one habit."""
    if len(habit.completion_dates) == 0:
        return 0

    dates = sorted(set(habit.completion_dates))

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(dates)):
        difference = dates[i] - dates[i - 1]

        if difference == timedelta(days=1):
            current_streak += 1

            if current_streak > longest_streak:
                longest_streak = current_streak
        else:
            current_streak = 1

    return longest_streak


def get_longest_streak_overall(habits):
    """Return the longest streak among all tracked habits."""
    if len(habits) == 0:
        return 0

    streaks = [get_longest_streak(habit) for habit in habits]
    return max(streaks)
