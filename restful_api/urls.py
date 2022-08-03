from django.urls import re_path, path
from restful_api.func.UserFunctions import userController
from restful_api.func.TokenFunctions import tokenController
from restful_api.func.BranchFunctions import branchController


urlpatterns = [
    re_path(r'^api/users$', userController.user_create),
    re_path(r'^api/token$', tokenController.token_create),
    re_path(
        r'^api/checkdev/(?P<username>[\w\-]+)/$', userController.user_check),
    re_path(r'^api/login$', userController.user_login),
    re_path(r'^api/authtoken/$', tokenController.tokenIdentify),
    re_path(r'^api/allbranches', branchController.getallbranch),

]
