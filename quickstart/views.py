from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from quickstart.serializers import UserSerializer, GroupSerializer


# viewsets -> 여러 view의 공통된 행동을 하나로 모아 class로 정의, 필요에 따라 개별뷰 분리 가능
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer   # serializers.py
    permission_classes = [permissions.IsAuthenticated]


# group -> 권한 프리셋!
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer  # serializers.py
    permission_classes = [permissions.IsAuthenticated]