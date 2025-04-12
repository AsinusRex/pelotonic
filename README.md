# Route Navigation System

A Python-based navigation system that connects users with optimal routes while incorporating real-time weather data and user preferences.

## Features

- **Navigation**: Find routes between locations using OpenStreetMap (OSM) tile system
- **Weather Integration**: Real-time weather data along routes via OpenMeteo API
- **User Profiles**: Track user preferences and journey statistics
- **Group Routing**: Support for individual and group-based routing preferences

## Architecture

The system consists of several components:

- **Database Layer**: MongoDB storage with geospatial indexing for map tiles
- **Area Data**: Functions for retrieving and connecting OSM tiles for route planning
- **User Management**: User profile storage, stats tracking, and group management
- **Weather Service**: Integration with OpenMeteo API for weather conditions

## Installation

```bash
# Clone the repository
git clone [repository-url]
cd [repository-name]

# Install dependencies
pip install -r requirements.txt

# Set up configuration
cp config.example.py config.py
# Edit config.py with your MongoDB URI and API keys
```

## Configuration

Edit `config.py` to include:

```python
# Database configuration
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "navigation_db"

# OpenMeteo API
WEATHER_API_KEY = "your_api_key"

# Map settings
MAP_ZOOM_LEVEL = 16  # Street-level detail
```

## Usage

```python
from db import connect, area_data

# Connect to database
db = connect()

# Find route tiles between two points
origin = {"lat": 40.7128, "lon": -74.0060}  # New York
destination = {"lat": 40.7484, "lon": -73.9857}  # Empire State
tiles = area_data.connect(origin, destination)

# Process route with weather data
# ...
```

## Dependencies

- Python 3.7+
- pymongo
- requests
- Other dependencies listed in requirements.txt

## License

[License information]