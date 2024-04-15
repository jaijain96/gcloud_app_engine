"""
defines user resource
"""
from flask import request, Response
from flask.views import MethodView
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from api.daos.user_dao import UserDao
from api.daos.bucket_list_dao import BucketListDao

import json

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user_dao = UserDao()
    user_obj = user_dao.get_user_from_db(
        username
    )
    # if not user_obj:
    #     return Response(response=f"user {user_id} doesn't exist", status=404)
    if user_obj and check_password_hash(user_obj.get("password"), password):
        return user_obj

class UserView(MethodView):
    def __init__(self):
        self.name_key = "user_view"
        self.user_dao = UserDao()
        self.bucket_list_dao = BucketListDao()

    # @auth.verify_password
    # def verify_password(self, username, password):
    #     user_obj = self.user_dao.get_user_from_db(
    #         username
    #     )
    #     # if not user_obj:
    #     #     return Response(response=f"user {user_id} doesn't exist", status=404)
    #     if user_obj and check_password_hash(user_obj.get("password"), password):
    #         return user_obj
    
    @auth.login_required
    def get(self, user_id):
        user_obj = auth.current_user()
        # user_obj = self.user_dao.get_user_from_db(
        #     user_id
        # )  # can use pydantic for request json parsing for type checks etc.
        if not user_obj:
            return Response(response=f"user {user_id} doesn't exist", status=404)

        return {"user": user_obj}

    def put(self, user_id):
        request_data = request.get_json()

        user_obj = self.user_dao.get_user_from_db(user_id)
        if user_obj:
            return Response(
                response=f"user {user_id} already exists",
                status=409,  # 409: conflict
            )

        # user_repr = {"name": request_data["name"]}
        user_repr = {"password": request_data["password"]}
        self.user_dao.put_user_into_db(user_id, user_repr)

        # self.bucket_list_dao.put_bucket_list_into_db(user_id, [])
        return Response(
            response=json.dumps({"user created": user_repr}),
            status=201,  # 201: created
        )

    def patch(self, user_id):
        request_data = request.get_json()

        user_obj = self.user_dao.get_user_from_db(user_id)
        if not user_obj:
            return Response(response=f"user {user_id} doesn't exist", status=404)

        # self.user_dao.update_user_in_db(user_id, request_data["name"])
        updates = {"name": request_data["name"]}
        updated_repr = self.user_dao.update_user_in_db(user_id, updates)
        if updated_repr:
            return {"user updated": updated_repr}
        else:
            return Response(response=f"unable to update user: {user_id}", status=500)

    def delete(self, user_id):
        user_obj = self.user_dao.get_user_from_db(user_id)
        if not user_obj:
            return Response(response=f"user {user_id} doesn't exist", status=404)

        # self.bucket_list_dao.delete_bucket_list_from_db(user_id)
        if self.user_dao.delete_user_from_db(user_id):
            return {"user deleted": user_obj}
        else:
            return Response(response=f"unable to delete user: {user_id}", status=500)
