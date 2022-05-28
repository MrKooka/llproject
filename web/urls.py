from .views import index_view
from django.urls import path,include,re_path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', index_view),
    path('api-token-auth/', obtain_jwt_token),
    
]
