from queue import Empty
from restful_api.models import Users
from restful_api.models import Tokenization
from restful_api.models import Branches
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
import string
import random
from restful_api.Serializers.tokenization_serializer import TokenizationSerializer


class GeneralParams:
    _filtered_username = ''
    _allFieldsSelected = []
    _field_token = []
    _field_token_afterSerializer = ''
    _field_last_id = 0
    _field_result = []
    _field_dynamic_result = []
    _field_branches = []


class GeneralHelper:
    def Slug(method, params, condition):
        match method:
            case 'POST':
                if condition == 'get/username':
                    return GeneralHelper._INIT_GET_USERNAME(params)
                elif condition == 'get/token':
                    return GeneralHelper._INIT_CHECKTOKEN(params)
            case 'GET':
                if condition == 'get/checktoken':
                    return GeneralHelper.__init_tokenidentify__(params)
                elif condition == 'api/getuser-info':
                    return GeneralHelper.__init_getcurrent_user(params)
                elif condition == 'api/get-all-branches':
                    helper = GeneralHelper()
                    helper.__init_findAllBranches()

    def TokenSlug(method, snapshot, access):
        match method:
            case 'POST':
                if access == 'tokenQueryBuild':
                    return QueryBuilder.tokenizationQueryBuild(snapshot)

    def _INIT_GET_USERNAME(params):
        users_list = Users.objects.filter(
            username=params).values()
        GeneralParams._allFieldsSelected = users_list
        return GeneralParams._allFieldsSelected

    def _INIT_CHECKTOKEN(params):
        token_list = Tokenization.objects.filter(
            userID=params).values()
        GeneralParams._field_token = token_list
        return GeneralParams._field_token

    def __init_tokenidentify__(userID):
        tokenize = Tokenization.objects.filter(
            userID=userID
        ).values()
        GeneralParams._field_result = tokenize
        return GeneralParams._field_result

    def __init_getcurrent_user(userid):
        users = Users.objects.filter(
            id=userid
        ).values()
        GeneralParams._field_dynamic_result = users
        return GeneralParams._field_dynamic_result

    def __init_findAllBranches(self):
        branches = Branches.objects.all().values().order_by('-id')
        GeneralParams._field_branches = branches
        return GeneralParams._field_branches


class SystemDecryptor:
    def decrypt(webpassword, hashpassword):
        return check_password(webpassword, hashpassword)


class QueryBuilder:
    def tokenizationQueryBuild(snapshot):
        tokenization = Tokenization()
        tokenization.userID = snapshot['userID']
        tokenization.token = snapshot['token']
        tokenization.lastRoute = snapshot['lastRoute']
        tokenization.isDestroyed = "0"
        tokenization.isvalid = "1"
        tokenization.save()
        GeneralParams._field_token_afterSerializer = "success_developer"
        return GeneralParams._field_token_afterSerializer


class SystemGenerator:
    def job(size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
