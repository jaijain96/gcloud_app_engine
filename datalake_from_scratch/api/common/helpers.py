import numpy as np
# from flask_httpauth import HTTPBasicAuth
# from werkzeug.security import generate_password_hash, check_password_hash


def load_dict(filepath):
    try:
        data_dict = np.load(filepath, allow_pickle=True).tolist()
        return data_dict
    except Exception as e:
        print(f"Exception occurring: {e}")
        return {}


def save_dict(data_dict, filepath):
    np.save(filepath, data_dict, allow_pickle=True)
    return True


# user_dict = load_dict("api/data/user_dict.npy")
# bucket_dict = load_dict("api/data/bucket_dict.npy")
# bucket_list_dict = load_dict("api/data/bucket_list_dict.npy")
# object_dict = load_dict("api/data/object_dict.npy")

# auth = HTTPBasicAuth()

# @auth.verify_password
# def verify_password(username, password):
#     if username in users and \
#             check_password_hash(users.get(username), password):
#     return username
