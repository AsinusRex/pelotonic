# This file has four functions, The first one is to create new users on the db.
# The second to fetch the user's data from the db.
# The third is to update the user's profile, including membership in groups. For example, on a daily basis he might need to ride on his own,
# but on weekends he might need to ride with a group one day, and another group another day.
# The fourth function is to calculate and update the user's stats after each journey.

# File: db/user_data.py
def create_user(user_info):
    # Stub for creating a new user in the database.
    print(f"Created user: {user_info}")
    return True

def get(user_id):
    # Stub for retrieving user data for the given user_id.
    print(f"Retrieving user data for: {user_id}")
    return {"user_id": user_id, "preferences": "default", "stats": {}}

def update_user_profile(user_id, profile_data):
    # Stub for updating the user's profile in the database.
    print(f"Updated profile for {user_id} with data: {profile_data}")
    return True

def update_user_stats(user_id, journey_data):
    # Stub for updating the user's stats after a journey.
    print(f"Updated stats for {user_id} with journey data: {journey_data}")
    return True