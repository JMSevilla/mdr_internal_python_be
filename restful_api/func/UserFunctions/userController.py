from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from restful_api.utils.helper import SystemGenerator
from restful_api.utils.helper import SystemDecryptor
from restful_api.utils.helper import GeneralHelper, GeneralParams

from restful_api.models import Users
from restful_api.serializer import UserSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def user_create(request):
    if request.method == 'POST':
        userserializer = UserSerializer(data=request.data)
        if userserializer.is_valid():
            userserializer.save()
            return Response({"message": "dev_registration_success", "data": userserializer.data}, status=status.HTTP_201_CREATED)
        return JsonResponse(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_check(request, username):
    if request.method == 'GET':
        get_username = Users.objects.filter(
            username=username)
        if get_username.exists():
            return Response({"message": "username_taken"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "username_available"}, status=status.HTTP_200_OK)

    else:
        return Response({"message": "empty_username_request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        if request.POST.get('role') == 'developer':
            username_rq = request.POST.get('username')
            password_rq = request.POST.get('password')
            GeneralHelper.Slug('POST', username_rq, 'get/username')
            users_list = GeneralParams._allFieldsSelected
            nodehelper = []
            tokerow = []
            if users_list:
                for node in users_list:
                    nodehelper = [
                        node['password'],
                        node['userType'],
                        node['isLock'],
                        node['id'],
                        node['firstname'],
                        node['lastname'],
                        node['username']
                    ]
                getdescrypted = SystemDecryptor.decrypt(password_rq, nodehelper[0])
                if getdescrypted:
                    if nodehelper[2] == '1':
                        return Response({"message": "ACCOUNT_LOCK"}, status=status.HTTP_200_OK)
                    else:
                        if nodehelper[1] == '2':
                            GeneralHelper.Slug(
                                'POST', nodehelper[3], 'get/token')
                            if GeneralParams._field_token.count() != 0:
                                for tokenode in GeneralParams._field_token:
                                    tokerow = [
                                        tokenode['isvalid']
                                    ]
                                if tokerow[0] == '1':
                                    return Response({"message": "valid"}, status=status.HTTP_200_OK)
                                else:
                                    collection = {
                                        "userID": nodehelper[3],
                                        "lastRoute": 'developer_platform',
                                        "token": SystemGenerator.job(50)
                                    }

                                    GeneralHelper.TokenSlug(
                                        'POST',
                                        collection,
                                        'tokenQueryBuild'
                                    )
                                    responseCollection = [
                                        nodehelper[4],
                                        nodehelper[5],
                                        nodehelper[6],
                                        'success_developer',
                                        'developer',
                                        nodehelper[3],
                                        GeneralParams._field_last_id
                                    ]
                                    return Response({"message": GeneralParams._field_token_afterSerializer,
                                                     'response_data': responseCollection}, status=status.HTTP_200_OK)
                            else:
                                collection = {
                                    "userID": nodehelper[3],
                                    "lastRoute": 'developer_platform',
                                    "token": SystemGenerator.job(50)
                                }
                                GeneralHelper.TokenSlug(
                                    'POST',
                                    collection,
                                    'tokenQueryBuild'
                                )
                                responseCollection = [
                                    nodehelper[4],
                                    nodehelper[5],
                                    nodehelper[6],
                                    'success_developer',
                                    'developer',
                                    nodehelper[3],
                                    GeneralParams._field_last_id
                                ]
                                return Response({"message": GeneralParams._field_token_afterSerializer,
                                                 'response_data': responseCollection}, status=status.HTTP_200_OK)

                else:
                    return Response({"message": "PASSWORD_INVALID"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "ACCOUNT_NOT_FOUND"}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "CLIENT_ACCOUNT"}, status=status.HTTP_200_OK)