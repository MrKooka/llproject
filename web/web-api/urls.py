from django.urls import path
from rest_framework import routers
from .views import GetWords,ExistWordView,DeleteWordView


# router = routers.SimpleRouter()

urlpatterns =[
    path('word/', GetWords.as_view()),
    path('existword/<str:w>', ExistWordView.as_view(), name='existword'),
    path('deleteword/<int:pk>',DeleteWordView.as_view(), name='deleteword')

]
# urlpatterns += router.urls  