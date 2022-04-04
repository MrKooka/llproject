from .views import index_view
from django.urls import path,include
urlpatterns = [
    path('word/', index_view),


    ]
