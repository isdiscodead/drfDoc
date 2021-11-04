from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Serializer -> Django의 Form, ModelForm과 비슷한 역할!
# response output 관리, instance와 queryset 다룸
# hyperlinked relation을 지원하는 Serializer -> PK보다 RESTful!
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
