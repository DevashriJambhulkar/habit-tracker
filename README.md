# Habit Tracker

## Project Description

Habit Tracker is a Python-based command-line application for creating,
managing, completing, and analysing habits.

The application supports daily and weekly habits and stores habit data
between sessions using a JSON file.

## Features

- Create a new habit
- Delete an existing habit
- Complete a habit
- Track habit creation date and completion date
- Support daily and weekly habits
- Store data in JSON
- Calculate longest streaks
- Show habits by periodicity
- Show longest streak overall
- Run unit tests

## Project Structure

- `main.py` - Runs the command-line application and displays the menu.
- `habit.py` - Contains the `Habit` class.
- `analytics.py` - Contains functions for habit analysis.
- `storage.py` - Saves and loads habit data using JSON.
- `habits.json` - Stores the saved habit data.
- `test_habit.py` - Contains unit tests for the application.

## Requirements

- Python 3.7 or newer

No additional Python packages are required.

## How to Run the Application

Open the project folder in the terminal and run:

```bash
python main.py