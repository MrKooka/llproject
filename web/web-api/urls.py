from django.urls import path
from rest_framework import routers
from .views import GetWords


router = routers.SimpleRouter()

urlpatterns =[
    path('word/', GetWords.as_view())
]
urlpatterns += router.urls  