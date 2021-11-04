from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views

# Routers provide an easy way of automatically determining the URL conf.
# r'문자열'은 rawstring으로, escape문 동작 X 그대로 출력
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 위에서 만든 router 자체를 추가
    path('', include(router.urls)),
    # Additionally, we include login URLs for the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
