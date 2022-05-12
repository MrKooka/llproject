from .views import index_view
from django.urls import path,include,re_path
urlpatterns = [
    re_path('^', index_view),
]
