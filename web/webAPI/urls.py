from django.urls import path
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from telegram import User

from .views import (
    GetWords,
    ExistWordView,
    DeleteWordView,
    GoogleAuthView,
    UserView,
    UpdateWordView,
    VoiceView
)


# router = routers.SimpleRouter()

urlpatterns =[
    path('word/', GetWords.as_view()),
    path('existword/<str:w>', ExistWordView.as_view(), name='existword'),
    path('deleteword/<int:pk>',DeleteWordView.as_view(), name='deleteword'),
    path('google/',GoogleAuthView.as_view(), name='googleAuth'),
    path('me/',UserView.as_view({"get":"retrieve","put":"update"})),
    path('updateWord/',UpdateWordView.as_view()),
    path('voice/<int:pk>',VoiceView.as_view())


    

    


]
# urlpatterns += router.urls  