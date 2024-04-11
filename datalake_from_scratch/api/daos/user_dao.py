from api.common.helpers import load_dict, save_dict
from api.daos.base_dao import BaseDao

class UserDao(BaseDao):
    def __init__(self):
        super().__init__()
        self.collection_ref = self.db.collection("users")

    def get_user_from_db(self, id):
        # user_dict = load_dict("api/data/user_dict.npy")
        doc_ref = self.collection_ref.document(id).get()
        if doc_ref.exists:
            return doc_ref.to_dict()

    def put_user_into_db(self, id, data):
        # user_dict = load_dict("api/data/user_dict.npy")
        # user_dict[id] = data
        # save_dict(user_dict, "api/data/user_dict.npy")
        doc_ref = self.collection_ref.document(id)
        doc_ref.set(data)
        return doc_ref.get().to_dict() == data

    def update_user_in_db(self, id, data: dict):
    # def update_user_in_db(self, id, name):
        # user_dict = load_dict("api/data/user_dict.npy")
        # user_dict[id]["name"] = name
        # save_dict(user_dict, "api/data/user_dict.npy")
        # return True
        doc_ref = self.collection_ref.document(id)
        doc_ref.set(data, merge=True)
        key_subset = set(data.keys())
        data_in_db = doc_ref.get().to_dict()
        key_superset = set(data_in_db.keys())
        if key_superset.intersection(key_subset) == key_subset:
            for key in key_subset:
                if data_in_db[key] != data[key]:
                    return False
        return data_in_db

    def delete_user_from_db(self, id):
        # user_dict = load_dict("api/data/user_dict.npy")
        # user_dict.pop(id)
        # save_dict(user_dict, "api/data/user_dict.npy")
        # return True
        doc_ref = self.collection_ref.document(id)
        doc_ref.delete()
        return not(doc_ref.get().exists)
