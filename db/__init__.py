from .area_data import AreaData
from .user_data import UserData
from .connect import Connect
import logging

class DB:
    def __init__(self):
        self._area = AreaData()
        self._user = UserData()
        self._connect = Connect()

    def check_in_db(self, db, bbox):
        return self._area.check_in_db(db, bbox)

    def write_graph_to_db(self, db, nodes, edges):
        return self._area.write_graph_to_db(db, nodes, edges)

    def get_user(self, db, user_id):
        return self._user.get(db, user_id)

    def connect(self, uri, db_name):
        return self._connect(uri, db_name)

db = DB()