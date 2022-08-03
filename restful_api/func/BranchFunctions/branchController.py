from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from restful_api.models import Branches

from restful_api.utils.helper import GeneralHelper, GeneralParams


@api_view(['GET'])
def getallbranch(self):
    GeneralHelper.Slug(
        'GET',
        None,
        'api/get-all-branches'
    )
    return Response({"message": GeneralParams._field_branches}, status=status.HTTP_200_OK)
