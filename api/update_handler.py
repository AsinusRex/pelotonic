# This handler will be called every time a client pings the server with their current location. It will return the
# location of other members of his group. It will also store the user's location in the db so we can later use it to
# process weights like usual speed, performance in slopes, etc.

from fastapi import APIRouter

router = APIRouter()

@router.post("/update")
def ping(location: dict):
    # Fake return of other users locations
    return {"group_members": [{"user_id": 1, "location": location}]}
