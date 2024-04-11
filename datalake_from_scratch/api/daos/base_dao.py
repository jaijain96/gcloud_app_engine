# from api.common.helpers import load_dict, save_dict
from google.cloud import firestore
import api.configs.config  as config
from typing import Self

class BaseDao:
    # """
    # problem: we want only one instance of BaseDao, every class that inherits this class will create an instance of BaseDao and multiple instances of firestore client which would be fairly heavy
    # """

    # def __new__(cls) -> Self:
    #     object_instance = super().__new__(cls)
    #     object_instance.db = firestore.Client(project=configs.config.PROJECT_ID)
    #     return object_instance
    
    def __init__(self):
        self.db = firestore.Client(project=config.PROJECT_ID, database=config.DATABASE_ID)

    # def get_user_from_db(self, id):
    #     user_dict = load_dict("api/data/user_dict.npy")
    #     return user_dict.get(id)

    # def put_user_into_db(self, id, data):
    #     user_dict = load_dict("api/data/user_dict.npy")
    #     user_dict[id] = data
    #     save_dict(user_dict, "api/data/user_dict.npy")
    #     return True

    # def update_user_in_db(self, id, name):
    #     user_dict = load_dict("api/data/user_dict.npy")
    #     user_dict[id]["name"] = name
    #     save_dict(user_dict, "api/data/user_dict.npy")
    #     return True

    # def delete_user_from_db(self, id):
    #     user_dict = load_dict("api/data/user_dict.npy")
    #     user_dict.pop(id)
    #     save_dict(user_dict, "api/data/user_dict.npy")
    #     return True
