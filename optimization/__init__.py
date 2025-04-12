# This file contains a single function that will return a weights object that will be used to calculate the route.
# It will get a list of the tiles involved. To do so it must first get the user data from the db to get the user's
# preferences and stats via db.user_data.get
# It will then use the weather and traffic data in the tile data to calculate the weights for the route. It will then
# return the weights object.


from db import user_data


def calculate_weights(user_id, tiles):
    user = user_data.get(user_id)
    return {"weights": "dummy_weights_based_on_user_preferences"}
