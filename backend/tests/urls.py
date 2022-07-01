from django.urls import path
from .views import *

urlpatterns = [
    path('languages/', Languages.as_view()),
    path('languages/choices/', LanguagesChoices.as_view()),
    path('question/<int:test_id>/', QuestionView.as_view()),
]