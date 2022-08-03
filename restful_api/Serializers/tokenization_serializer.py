from rest_framework import serializers
from restful_api.models import Tokenization


class TokenizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tokenization
        fields = (
            'id',
            'userID',
            'token',
            'lastRoute',
            'isDestroyed',
            'isvalid',
            'created_at',
            'updated_at'
        )

    def create(self, validated_data):
        userID = validated_data.get('userID')
        token = validated_data.get('token')
        lastRoute = validated_data.get('lastRoute')
        isDestroyed = '0'
        isvalid = '1'
        tokenization = Tokenization.objects.create(
            userID=userID,
            token=token,
            lastRoute=lastRoute,
            isDestroyed=isDestroyed,
            isvalid=isvalid
        )
        return tokenization

    def initial_create(self, validated_data):
        userID = validated_data.get('userID')
        token = validated_data.get('token')
        lastRoute = validated_data.get('lastRoute')
        isDestroyed = '0'
        isvalid = '1'
        tokenization = Tokenization.objects.create(
            userID=userID,
            token=token,
            lastRoute=lastRoute,
            isDestroyed=isDestroyed,
            isvalid=isvalid
        )
        return tokenization
