import logging


class UserData:
    @staticmethod
    def get(db, user_id: str):
        """
        Retrieves user data from the 'users' collection in the database.

        Parameters:
          db: The MongoDB database instance as returned from the connection.
          user_id: The unique identifier for the user.

        Returns:
          A dictionary containing the user data if found; otherwise, None.
        """
        try:
            user_data = db["users"].find_one({"_id": user_id})
            if user_data:
                return user_data
            else:
                logging.info("User %%s not found in the database.", user_id)
                return None
        except Exception as e:
            logging.error("Error retrieving user data for %%s: %%s", user_id, e)
            return None

    @staticmethod
    def set(db, user_id: str, user_data: dict):
        print("User  data set")