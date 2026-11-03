import unittest
from datetime import date

from habit import Habit
from analytics import (
    get_longest_streak,
    get_longest_streak_overall,
    get_habits_by_periodicity
)


class TestHabit(unittest.TestCase):

    def test_create_habit(self):
        habit = Habit("Read Book", "daily")

        self.assertEqual(habit.name, "Read Book")
        self.assertEqual(habit.periodicity, "daily")
        self.assertFalse(habit.completed)

    def test_complete_habit(self):
        habit = Habit("Exercise", "daily")

        habit.complete_habit()

        self.assertTrue(habit.completed)
        self.assertIsNotNone(habit.completed_at)

    def test_add_completion_date(self):
        habit = Habit("Drink Water", "daily")

        completion_date = date(2026, 10, 1)
        habit.add_completion_date(completion_date)

        self.assertIn(completion_date, habit.completion_dates)
        self.assertTrue(habit.completed)

    def test_longest_streak(self):
        habit = Habit("Study", "daily")

        habit.add_completion_date(date(2026, 10, 1))
        habit.add_completion_date(date(2026, 10, 2))
        habit.add_completion_date(date(2026, 10, 3))

        streak = get_longest_streak(habit)

        self.assertEqual(streak, 3)

    def test_empty_streak(self):
        habit = Habit("Meditate", "daily")

        streak = get_longest_streak(habit)

        self.assertEqual(streak, 0)

    def test_longest_streak_overall(self):
        habit1 = Habit("Drink Water", "daily")
        habit2 = Habit("Exercise", "daily")

        habit1.add_completion_date(date(2026, 10, 1))
        habit1.add_completion_date(date(2026, 10, 2))
        habit1.add_completion_date(date(2026, 10, 3))

        habit2.add_completion_date(date(2026, 10, 1))

        streak = get_longest_streak_overall([habit1, habit2])

        self.assertEqual(streak, 3)

    def test_habits_by_periodicity(self):
        habit1 = Habit("Drink Water", "daily")
        habit2 = Habit("Exercise", "daily")
        habit3 = Habit("Clean Room", "weekly")

        habits = [habit1, habit2, habit3]

        daily_habits = get_habits_by_periodicity(habits, "daily")

        self.assertEqual(len(daily_habits), 2)
        self.assertIn(habit1, daily_habits)
        self.assertIn(habit2, daily_habits)
        self.assertNotIn(habit3, daily_habits)

if __name__ == "__main__":
    unittest.main()