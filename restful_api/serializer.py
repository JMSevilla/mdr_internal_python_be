from rest_framework import serializers
from restful_api.models import Users
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'firstname',
            'lastname',
            'username',
            'password',
            'userType',
            'isLock',
            'imgURL',
            'occupationStatus',
            'occupationDetails',
            'occupationPositionWork',
            'nameofschool',
            'degree',
            'address',
            'created_at',
            'updated_at'
        )

    def create(self, validated_data):
        firstname = validated_data.get('firstname')
        lastname = validated_data.get('lastname')
        username = validated_data.get('username')
        password = validated_data.get('password')
        userType = '2'
        isLock = '1'
        imgURL = 'None'
        occupationStatus = validated_data.get('occupationStatus')
        occupationDetails = validated_data.get('occupationDetails')
        occupationPositionWork = validated_data.get('occupationPositionWork')
        nameofschool = validated_data.get('nameofschool')
        degree = validated_data.get('degree')
        address = validated_data.get('address')
        users = Users.objects.create(
            firstname=firstname,
            lastname=lastname,
            username=username,
            password=make_password(password),
            userType=userType,
            isLock=isLock,
            imgURL=imgURL,
            occupationStatus=occupationStatus,
            occupationDetails=occupationDetails,
            occupationPositionWork=occupationPositionWork,
            nameofschool=nameofschool,
            degree=degree,
            address=address
        )
        return users
