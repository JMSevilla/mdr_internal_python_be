from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from restful_api.models import Tokenization
from restful_api.Serializers.tokenization_serializer import TokenizationSerializer
from rest_framework.decorators import api_view

from restful_api.utils.helper import GeneralHelper, GeneralParams


@api_view(['POST'])
def token_create(request):
    if request.method == 'POST':
        serializer = TokenizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tokenIdentify(request):
    account_userid = request.GET.get('userid')
    if account_userid == 'unknown':
        return Response({
            "message": "invalid_token"
        }, status=status.HTTP_200_OK)
    elif account_userid == 'unknown1':
        return Response({
            "message": "invalid_token"
        }, status=status.HTTP_200_OK)
    else:
        GeneralHelper.Slug(
            'GET',
            account_userid,
            'get/checktoken'
        )
        iterate = GeneralParams._field_result
        selectedField = []
        dynamicField = []
        if not bool(iterate):
            return Response({"message" : "empty_array"}, status=status.HTTP_200_OK)
        else:
            for field in iterate:
                selectedField = [
                    field['isvalid'],
                    field['lastRoute']
                ]
            if selectedField[0] == '1':
                if selectedField[1] == 'developer_platform':
                    GeneralHelper.Slug(
                        'GET',
                        account_userid,
                        'api/getuser-info'
                    )
                    for dynamicFieldSelected in GeneralParams._field_dynamic_result:
                        dynamicField = [
                            dynamicFieldSelected['firstname'],
                            dynamicFieldSelected['lastname'],
                            dynamicFieldSelected['username'],
                            dynamicFieldSelected['imgURL'],
                            dynamicFieldSelected['id'],
                            selectedField[1],
                            'token_exist_dev_platform'
                        ]
                    return Response({
                        "message" : dynamicField
                    }, status=status.HTTP_200_OK)
                elif selectedField[1] == '/developer/dashboard':
                    GeneralHelper.Slug(
                        'GET',
                        account_userid,
                        'api/getuser-info'
                    )
                    for dynamicFieldSelected in GeneralParams._field_dynamic_result:
                        dynamicField = [
                            dynamicFieldSelected['firstname'],
                            dynamicFieldSelected['lastname'],
                            dynamicFieldSelected['username'],
                            dynamicFieldSelected['imgURL'],
                            dynamicFieldSelected['id'],
                            selectedField[1],
                            'token_exist_dev_platform'
                        ]
                    return Response({
                        "message": dynamicField
                    }, status=status.HTTP_200_OK)

        return Response({
            "data": GeneralParams._field_result
        }, status=status.HTTP_200_OK)
