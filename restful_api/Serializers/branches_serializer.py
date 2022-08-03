from rest_framework import serializers
from restful_api.models import Branches


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = (
            'id',
            'branchName',
            'branchDescription',
            'branchImg',
            'branchRoute',
            'branchIsActive',
            'created_at',
            'updated_at'
        )
