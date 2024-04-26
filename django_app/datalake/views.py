from django.db.utils import IntegrityError
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.views import View
from datalake import models
import json

# Create your views here.
class UserView(View):
    # def __init__(self):
    #     self.name_key = "user_view"
    #     self.user_dao = UserDao()
    #     self.bucket_list_dao = BucketListDao()

    # # @auth.verify_password
    # # def verify_password(self, username, password):
    # #     user_obj = self.user_dao.get_user_from_db(
    # #         username
    # #     )
    # #     # if not user_obj:
    # #     #     return Response(response=f"user {user_id} doesn't exist", status=404)
    # #     if user_obj and check_password_hash(user_obj.get("password"), password):
    # #         return user_obj
    
    # @auth.login_required
    # def get(self, user_id):
    #     user_obj = auth.current_user()
    #     # user_obj = self.user_dao.get_user_from_db(
    #     #     user_id
    #     # )  # can use pydantic for request json parsing for type checks etc.
    #     if not user_obj:
    #         return Response(response=f"user {user_id} doesn't exist", status=404)

    #     return {"user": user_obj}

    ###########

    # def __init__(self):
    #     self.name_key = "user_view"
    #     self.user_dao = UserDao()
    #     self.bucket_list_dao = BucketListDao()

    # @auth.verify_password
    # def verify_password(self, username, password):
    #     user_obj = self.user_dao.get_user_from_db(
    #         username
    #     )
    #     # if not user_obj:
    #     #     return Response(response=f"user {user_id} doesn't exist", status=404)
    #     if user_obj and check_password_hash(user_obj.get("password"), password):
    #         return user_obj
    
    def get(self, request, user_id):
        try:
            user_model = models.User.objects.get(name=user_id)
        except models.User.DoesNotExist:
            # return Response(response=f"user {user_id} doesn't exist", status=404)
            raise Http404(f"user {user_id} doesn't exist")

        # user_obj = auth.current_user()
        # user_obj = self.user_dao.get_user_from_db(
        #     user_id
        # )  # can use pydantic for request json parsing for type checks etc.
        # if not user_obj:
        #     return Response(response=f"user {user_id} doesn't exist", status=404)
        return HttpResponse(json.dumps({"name": user_model.name}))

    def put(self, request, user_id):
        request_body = json.loads(request.body.decode())
        try:
            models.User.objects.create(name=user_id, password=request_body["password"])
            return HttpResponse(f"user {user_id} created")
        except IntegrityError:
            return HttpResponseBadRequest(f"user {user_id} already exists")
        # request_data = request.get_json()

        # user_obj = self.user_dao.get_user_from_db(user_id)
        # if user_obj:
        #     return Response(
        #         response=f"user {user_id} already exists",
        #         status=409,  # 409: conflict
        #     )

        # # user_repr = {"name": request_data["name"]}
        # user_repr = {"password": request_data["password"]}
        # self.user_dao.put_user_into_db(user_id, user_repr)

        # # self.bucket_list_dao.put_bucket_list_into_db(user_id, [])
        # return Response(
        #     response=json.dumps({"user created": user_repr}),
        #     status=201,  # 201: created
        # )

    # def patch(self, user_id):
    #     request_data = request.get_json()

    #     user_obj = self.user_dao.get_user_from_db(user_id)
    #     if not user_obj:
    #         return Response(response=f"user {user_id} doesn't exist", status=404)

    #     # self.user_dao.update_user_in_db(user_id, request_data["name"])
    #     updates = {"name": request_data["name"]}
    #     updated_repr = self.user_dao.update_user_in_db(user_id, updates)
    #     if updated_repr:
    #         return {"user updated": updated_repr}
    #     else:
    #         return Response(response=f"unable to update user: {user_id}", status=500)

    # def delete(self, user_id):
    #     user_obj = self.user_dao.get_user_from_db(user_id)
    #     if not user_obj:
    #         return Response(response=f"user {user_id} doesn't exist", status=404)

    #     # self.bucket_list_dao.delete_bucket_list_from_db(user_id)
    #     if self.user_dao.delete_user_from_db(user_id):
    #         return {"user deleted": user_obj}
    #     else:
    #         return Response(response=f"unable to delete user: {user_id}", status=500)
