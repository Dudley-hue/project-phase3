# Weather Application
This project is a simple CLI-based weather application that allows users to manage weather and forecast data for different cities. The application uses SQLAlchemy for ORM and SQLite as the database.

# Features
Add, view, update, and delete city information
Add, view, and delete weather data for cities
Add, view, and delete forecast data for cities
View weather and forecast data within a specified date range
# Prerequisites
Python 3.6 or higher
Pipenv for managing the virtual environment and dependencies
# Project Structure
graphql
weather_app/
│
├── cli.py            # CLI commands for the application
├── models.py         # SQLAlchemy models and database setup
├── Pipfile           # Pipenv configuration file
├── Pipfile.lock      # Pipenv lock file
└── weather.db        # SQLite database file (generated after initialization)
# Installation
 # Clone the repository:
git clone (https://github.com/Dudley-hue/project-phase3.git)
cd weather_app
Set up the virtual environment and install dependencies:
pipenv install
# Activate the virtual environment:
pipenv shell
# Initialize the database:
pipenv run python cli.py initdb
# Usage
Available Commands
# Initialize the database:
pipenv run python cli.py initdb
This command initializes the database and creates the necessary tables.

# Add a city:
pipenv run python cli.py add-city "City Name"
# Add weather data:
pipenv run python cli.py add-weather "City Name" Temperature "Description"
 # Add forecast data:
pipenv run python cli.py add-forecast "City Name" "Forecast"
 # View weather data:
pipenv run python cli.py view-weather "City Name" --start-date YYYY-MM-DD --end-date YYYY-MM-DD
Both --start-date and --end-date options are optional.

# View forecast data:
pipenv run python cli.py view-forecast "City Name" --start-date YYYY-MM-DD --end-date YYYY-MM-DD
Both --start-date and --end-date options are optional.
# Update city name:
pipenv run python3 cli.py update-city "Old City Name" "New City Name"
# Delete a city:
pipenv run python3 cli.py delete-city "City Name"
# Delete weather data:
pipenv run python3 cli.py delete-weather "City Name" "YYYY-MM-DD"
# Delete forecast data:
pipenv run python3 cli.py delete-forecast "City Name" "YYYY-MM-DD"
# Add cities:
pipenv run python3 cli.py add-city "New York"
pipenv run python3 cli.py add-city "London"
# Add weather data:
pipenv run python3 cli.py add-weather "New York" 25 "Sunny"
pipenv run python3 cli.py add-weather "London" 20 "Cloudy"
 # Add forecast data:
pipenv run python3 cli.py add-forecast "New York" "Rain expected tomorrow"
pipenv run python3 cli.py add-forecast "London" "Partly cloudy skies"
# View weather data:
pipenv run python3 cli.py view-weather "New York"
# View forecast data:
pipenv run python3 cli.py view-forecast "London"
# Update a city's name:
pipenv run python3 cli.py update-city "New York" "NYC"
# Delete a city:
pipenv run python3 cli.py delete-city "London"
# Delete weather data:
pipenv run python3 cli.py delete-weather "NYC" "2023-06-13"
# Delete forecast data:
pipenv run python3 cli.py delete-forecast "NYC" "2023-06-13"
# License
This project is licensed under the MIT License - see the LICENSE file for details.