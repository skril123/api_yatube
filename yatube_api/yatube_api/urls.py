from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', obtain_auth_token),
    path('api/v1/', include('api.urls')),
]