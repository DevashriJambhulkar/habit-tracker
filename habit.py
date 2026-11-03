from datetime import datetime


class Habit:
    """Represent a habit that can be tracked by the application."""

    def __init__(self, name, periodicity):
        """Create a new habit."""
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completed = False
        self.completed_at = None
        self.completion_dates = []

    def show_habit(self):
        """Display the information of the habit."""
        print("Name:", self.name)
        print("Periodicity:", self.periodicity)
        print("Created at:", self.created_at)
        print("Completed:", self.completed)
        print("Completed at:", self.completed_at)
        print("Completion dates:", self.completion_dates)

    def complete_habit(self):
        """Mark the habit as completed and record the completion time."""
        self.completed = True
        self.completed_at = datetime.now()
        self.completion_dates.append(self.completed_at.date())

    def add_completion_date(self, completion_date):
        """Add an example or historical completion date."""
        self.completion_dates.append(completion_date)
        self.completed = True
        self.completed_at = datetime.combine(
            completion_date,
            datetime.min.time()
        )

    def to_dict(self):
        """Convert the habit into a dictionary for JSON storage."""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completed": self.completed,
            "completed_at": (
                self.completed_at.isoformat()
                if self.completed_at
                else None
            ),
            "completion_dates": [
                completion_date.isoformat()
                for completion_date in self.completion_dates
            ]
        }