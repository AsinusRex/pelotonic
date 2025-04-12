# This file contains one function that takes a list of tiles in the db that contain all the nodes and edges it needs
# to make a route, as well as the weights object it will need to take into account. It returns the route in a format the
# client can display it.

def plot(tiles, weights):
    return {"route": ["pointA", "pointB"], "weights": weights}